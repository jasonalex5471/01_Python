import numpy as np
import time
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# 1. 轨迹生成
def generate_path(text="loveLily", density=150):
    font_path = r"C:\Windows\Fonts\arial.ttf"
    font_prop = FontProperties(fname=font_path, weight='bold')
    tp = TextPath((0, 0), text, size=1, prop=font_prop)
    
    polys = tp.to_polygons()
    
    segments = []
    for poly in polys:
        seg = []
        for i in range(len(poly) - 1):
            p1, p2 = poly[i], poly[i+1]
            num = max(2, int(np.linalg.norm(p2 - p1) * density))
            for t in np.linspace(0, 1, num):
                seg.append(p1 + t*(p2-p1))
        if seg:
            segments.append(np.array(seg))

    all_pts = np.vstack(segments)
    xmin, xmax = np.min(all_pts[:,0]), np.max(all_pts[:,0])
    ymin, ymax = np.min(all_pts[:,1]), np.max(all_pts[:,1])
    text_w, text_h = xmax - xmin, ymax - ymin
    
    # 锚定工作区
    target_x, target_y, target_w, target_h = 0.9, 0.0, 0.8, 0.3
    scale = min(target_w / text_w, target_h / text_h)
    
    res = []
    for seg in segments:
        mapped_seg = []
        for pt in seg:
            x = target_x + (pt[0] - (xmin + text_w/2)) * scale
            y = target_y + (pt[1] - (ymin + text_h/2)) * scale
            mapped_seg.append([x, y])
        res.append(np.array(mapped_seg))
    return res

# 2. 解析逆运动学
def ik_solve(x, y, L1=1.0, L2=0.8):
    cos_q2 = np.clip((x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2), -1.0, 1.0)
    q2 = -np.arccos(cos_q2)
    q1 = np.arctan2(y, x) - np.arctan2(L2*np.sin(q2), L1+L2*np.cos(q2))
    return [q1, q2]

# 3. 主控逻辑
def main():
    print("正在建立 ZeroMQ 同步连接...")
    client = RemoteAPIClient()
    sim = client.getObject('sim')

    if sim.getSimulationState() != sim.simulation_stopped:
        sim.stopSimulation()
        while sim.getSimulationState() != sim.simulation_stopped:
            time.sleep(0.1)

    for i in range(100):
        try: sim.removeDrawingObject(i)
        except: pass

    # 开启步进同步模式
    client.setStepping(True) 
    sim.startSimulation()

    j1 = sim.getObject('/Joint1')
    j2 = sim.getObject('/Joint1/Link1/Joint2')
    pen = sim.getObject('/Joint1/Link1/Joint2/Link2/PenTip')

    line_h = sim.addDrawingObject(sim.drawing_lines, 5, 0, -1, 99999, [0, 0, 1])
    
    path = generate_path("loveLily")
    pen_z = sim.getObjectPosition(pen, -1)[2]

    curr_x, curr_y = path[0][0][0], path[0][0][1]
    curr_q = ik_solve(curr_x, curr_y)
    sim.setJointPosition(j1, float(curr_q[0]))
    sim.setJointPosition(j2, float(curr_q[1]))
    sim.step()

    print("启动高精度逐帧动画绘制，请欣赏...")
    frame_counter = 0
    
    for seg in path:
        start_pt = seg[0]
        
        # A. 抬笔跳跃转场
        steps_up = 60
        for i in range(1, steps_up + 1):
            ix = curr_x + (start_pt[0] - curr_x) * (i / steps_up)
            iy = curr_y + (start_pt[1] - curr_y) * (i / steps_up)
            q = ik_solve(ix, iy)
            sim.setJointPosition(j1, float(q[0]))
            sim.setJointPosition(j2, float(q[1]))
            sim.step()
            time.sleep(0.01)
            
        curr_x, curr_y = start_pt[0], start_pt[1]
        last_p = [float(curr_x), float(curr_y), float(pen_z)]
        
        # B. 稳定落笔绘制
        for pt in seg:
            q = ik_solve(pt[0], pt[1])
            sim.setJointPosition(j1, float(q[0]))
            sim.setJointPosition(j2, float(q[1]))
            
            curr_x, curr_y = pt[0], pt[1]
            curr_p = [float(curr_x), float(curr_y), float(pen_z)]
            
            sim.addDrawingObjectItem(line_h, last_p + curr_p)
            last_p = curr_p
            
            frame_counter += 1
            if frame_counter % 2 == 0:
                sim.step()
                time.sleep(0.005) 

    print("Task 7.2 数字孪生书法展示完毕。")

if __name__ == "__main__":
    main()
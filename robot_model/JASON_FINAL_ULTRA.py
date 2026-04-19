import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.textpath import TextPath
from spatialmath import SE3
from roboticstoolbox.backends.PyPlot import PyPlot

# 1：全局路径生成
def get_path_data(text="Jason", density=60):
    tp = TextPath((0, 0), text, size=1)
    all_v, all_c = tp.vertices, tp.codes
    
    xmin, xmax = np.min(all_v[:,0]), np.max(all_v[:,0])
    ymin, ymax = np.min(all_v[:,1]), np.max(all_v[:,1])

    segments = []
    curr = []
    
    for i in range(len(all_v)):
        code = all_c[i]
        
        if code == 1: # MOVETO (抬笔，开始新轮廓)
            if curr: segments.append(np.array(curr))
            curr = [all_v[i]]
            
        elif code == 79: # CLOSEPOLY (闭合当前轮廓)
            if curr:
                p1 = curr[-1]
                p2 = curr[0] 
                num = max(2, int(np.linalg.norm(p2-p1)*density))
                for t in np.linspace(0, 1, num):
                    curr.append(p1 + t*(p2-p1))
                segments.append(np.array(curr))
                curr = [] # 闭合后清空，等待下一个 MOVETO
                
        else: # LINETO / CURVE (正常画线)
            if not curr:
                curr = [all_v[i]]
                continue
            p1 = curr[-1]
            p2 = all_v[i]
            num = max(2, int(np.linalg.norm(p2-p1)*density))
            for t in np.linspace(0, 1, num):
                curr.append(p1 + t*(p2-p1))
                
    if curr: segments.append(np.array(curr))

    # 映射到机器人工作空间
    final_segments = []
    for seg in segments:
        x = 0.7 + (seg[:,0] - xmin) / (xmax - xmin) * 0.8
        z = -0.3 + (seg[:,1] - ymin) / (ymax - ymin) * 0.6
        final_segments.append(np.column_stack((x, z)))
        
    return final_segments
# 2：机器人建模
def create_robot():
    # 大臂 1.0m, 小臂 0.8m
    l1 = rtb.RevoluteDH(a=1.0)
    l2 = rtb.RevoluteDH(a=0.8,qlim=[-np.pi,-0.01])
    robot = rtb.DHRobot([l1, l2], name="Jason_Painter_V3")
    robot.base = SE3.Rx(np.pi/2)
    return robot

# 3：平滑仿真 (解决回弹与轨迹连续性)
def run_and_export():
    robot = create_robot()
    path_segments = get_path_data()
    
    env = PyPlot()
    env.launch(name="Final Report: Jason Robot")
    env.add(robot)
    ax = env.ax
    ax.view_init(elev=0, azim=-90)
    
    robot.q = np.array([0.4, -0.4]) 
    full_q_history = []

    print("--- 启动工业级平滑仿真 ---")
    
    for seg in path_segments:
        T_start = SE3(seg[0,0], 0, seg[0,1])
        sol_start = robot.ikine_LM(T_start, q0=robot.q, mask=[1,1,1,0,0,0])
        
        if sol_start.success:
            q_transition = rtb.jtraj(robot.q, sol_start.q, 20).q
            for q_step in q_transition:
                robot.q = q_step
                full_q_history.append(np.degrees(q_step))
                env.step(0.01)

        for p in seg:
            if not plt.fignum_exists(env.fig.number): break
            
            T_target = SE3(p[0], 0, p[1])
            sol = robot.ikine_LM(T_target, q0=robot.q, mask=[1,1,1,0,0,0])
            
            if sol.success:
                robot.q = sol.q
                full_q_history.append(np.degrees(sol.q))
                ax.plot(p[0], 0, p[1], 'b.', markersize=2)
                env.step(0.005)

    # 4：成果自动保存
    if full_q_history:
        df = pd.DataFrame(full_q_history, columns=['Shoulder_q1', 'Elbow_q2'])
        df.to_csv('jason_robot_data_v3.csv', index=False)
        print("\n[成功] 数据已保存至 jason_robot_data_v3.csv")
        
        plt.figure(figsize=(10, 5))
        plt.plot(df['Shoulder_q1'], label='Joint 1 (Shoulder)', alpha=0.8)
        plt.plot(df['Elbow_q2'], label='Joint 2 (Elbow)', alpha=0.8)
        plt.title('Final Smooth Trajectory Analysis')
        plt.xlabel('Step Count')
        plt.ylabel('Angle (Degrees)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.savefig('final_smooth_curves.png')
        print("[成功] 曲线图已保存至 final_smooth_curves.png")

    print("实验演示结束。")
    env.hold()

if __name__ == "__main__":
    run_and_export()
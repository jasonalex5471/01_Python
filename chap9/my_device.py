class Device:
    """It's a device class"""
    def __init__(self,name,id_code):
       """init the class"""
       self.name = name
       self.id_code = id_code
       self.status = 'idel'
       
    def describe_device(self):
        """describe the device"""
        print(f"device name:{self.name}")
        print(f"id_code:{self.id_code}")
        print(f"status:{self.status}")
        
    def activate(self):
        """change the status"""
        self.status = 'running'
        
    def update_status(self,new_status):
        """update status"""
        self.status = new_status
        
class DeepLearningServer(Device):
    """the device only for deeplearning"""
    def __init__(self, name, id_code):
        super().__init__(name, id_code)
        self.gpu_model = 'RTX 4090'

    def describe_device(self):
        super().describe_device()
        print(f"gpu_model:{self.gpu_model}")

    def train_model(self):
        """training movement"""
        print(f"turn on the device")
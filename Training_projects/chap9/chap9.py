from Training_projects.chap9.my_device import Device as DV
from Training_projects.chap9.my_device import DeepLearningServer as DS

my_device = DV('lightning',12)
deeplearning = DS('DeepLearningServer',10)

my_device.describe_device()
deeplearning.describe_device()

my_device.activate()
my_device.describe_device()

my_device.update_status('turning off')
my_device.describe_device()

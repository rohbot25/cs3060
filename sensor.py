import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.sensorValues = numpy.zeros(c.iterations)
    def Get_Value(self,t):
        self.sensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save("data/"+self.linkName+".npy",self.sensorValues)

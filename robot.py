import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
from sensor import SENSOR
from motor import MOTOR
class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        
    def Prepare_To_Sense(self):
        self.sensors = dict()
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self,t):
        for key in self.sensors:
            self.sensors[key].Get_Value(t)
    def Prepare_To_Act(self):
        self.motors = dict()
        for jointName in pyrosim.jointNamesToIndices:
            print(type(jointName))
            self.motors[jointName.decode('ASCII')] = MOTOR(jointName)
        print(self.motors)
    def Act(self,desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if(self.nn.Is_Motor_Neuron(neuronName)):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle,self.robotId)
                print("act",desiredAngle)
    def Think(self,t):
        self.nn.Update()
        self.nn.Print()
        

        
            
            
            
        

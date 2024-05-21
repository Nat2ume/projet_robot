from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Mouvement():
    def __init__(self):
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.C)
        self.bras = Motor(Port.B)

    def avancer(self):
        self.left_motor.run(500)
        self.right_motor.run(500)

    def reculer(self):
        self.left_motor.run(-500)
        self.right_motor.run(-500)

    def gauche(self):
        self.left_motor.run(-100)
        self.right_motor.run(100)

    def droite(self):
        self.left_motor.run(100)
        self.right_motor.run(-100)
    
    def stop(self):
        self.left_motor.run(0)
        self.right_motor.run(0)
        self.bras.run(0)
    
    def lever_bras(self):
        self.bras.run(50)
    
    def baisser_bras(self):
        self.bras.run(-50)

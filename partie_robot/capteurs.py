#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class Capteur():
    def __init__ (self) :
        self.color_sensor = ColorSensor(Port.S3)
        self.us = UltrasonicSensor(Port.S2)
        self.gs = GyroSensor(Port.S4, Direction.CLOCKWISE)

    def capteur_lumiere(self):
        if self.color_sensor.reflection() > 12 :
            return False
        return self.color_sensor.reflection()
    
    def obstacle (self) :
        if self.us.distance() < 130 :
            return True
        return False
    
    def gyroscope (self) :
        return self.gs.angle()
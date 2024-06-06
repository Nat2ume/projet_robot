#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import serveur

if __name__ == "__main__":
    #Create your objects here.
    print("coucou ici")
    ev3 = EV3Brick()
    print("coucou la")
    robot = serveur.Serveur(1664)
    robot.recevoir()

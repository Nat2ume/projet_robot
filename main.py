#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import socket




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


class Serveur():
    def __init__(self, port):
        self.ADRESSE = ""
        self.PORT = port
        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serveur.bind((self.ADRESSE, self.PORT))
        self.serveur.listen(10)
        self.moteur = Mouvement()
        self.capteur = Capteur()
    
    def recevoir(self):
        fin = False
        while fin == False:
            # Attente qu'un client se connecte
            client, adresse = self.serveur.accept()

            # Réception de la requete du client sous forme de bytes et transformation en string
            requete = client.recv(1024)
            if requete.decode() == "AVANCER":
                self.moteur.avancer()
            if requete.decode() == "RECULER":
                self.moteur.reculer()
            if requete.decode() == "GAUCHE":
                self.moteur.gauche()
            if requete.decode() == "DROITE":
                self.moteur.droite()
            if requete.decode() == "LEVERBRAS":
                self.moteur.lever_bras()
            if requete.decode() == "BAISSERBRAS":
                self.moteur.baisser_bras()
            if requete.decode() == "STOP":
                self.moteur.stop()
            if requete.decode() == "X":
                self.moteur.stop()
                fin = True

            # Déconnexion avec le client
            client.close()
            
        # Arrêt du serveur 
        serveur.close()



if __name__ == "__main__":
    # Create your objects here.
    ev3 = EV3Brick()
    robot = Serveur(1664)
    robot.recevoir()

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import socket


# Create your objects here.
ev3 = EV3Brick()

class Mouvement():
    def __init__(self):
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.C)

    def avancer(self):
        self.left_motor.run(500)
        self.right_motor.run(500)

    def reculer(self):
        self.left_motor.run(-500)
        self.right_motor.run(-500)

    def gauche(self):
        self.left_motor.run(-200)
        self.right_motor.run(200)

    def droite(self):
        self.left_motor.run(200)
        self.right_motor.run(-200)
    
    def stop(self):
        self.left_motor.run(0)
        self.right_motor.run(0)



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


if __name__ == "__main__":
    # Interface réseau et port TCP d'acoute
    ADRESSE = ""
    PORT = 1664

    # Création d'une socket
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configuration de la socket pour pouvoir la réutiliser
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # On demande à l'OS d'attacher notre programme au port TCP demandé
    serveur.bind((ADRESSE, PORT))
    serveur.listen(10)

    moteur = Mouvement()
    capteur = Capteur()

    # Boucle de gestion des connexions des clients
    fin = False
    while fin == False:
        # Attente qu'un client se connecte
        client, adresse = serveur.accept()

        # Réception de la requete du client sous forme de bytes et transformation en string
        requete = client.recv(1024)
        if requete.decode() == "AVANCER":
            moteur.avancer()
        if requete.decode() == "RECULER":
            moteur.reculer()
        if requete.decode() == "GAUCHE":
            moteur.gauche()
        if requete.decode() == "DROITE":
            moteur.droite()
        if requete.decode() == "STOP":
            moteur.stop()

            
        # Déconnexion avec le client
        print("Fermeture de la connexion avec le client.")
        client.close()

    # Arrêt du serveur    
    print("Arret du serveur.")
    serveur.close()
"""
NSI :: Client TCP
"""

# Librairie(s)
import socket

class Client():
    def __init__(self, ip_robot, port):
        self.HOST = ip_robot
        self.PORT = 1664
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def envoie(self, requete):
        self.client.connect((self.HOST, self.PORT))
        self.client.send(requete.encode())
        self.client.close()
    
    def avancer(self):
        requete = "AVANCER"
        self.envoie(requete)

    def reculer(self):
        requete = "RECULER"
        self.envoie(requete)
    
    def tourner_droit(self):
        requete = "DROITE"
        self.envoie(requete)
    
    def tourner_gauche(self):
        requete = "GAUCHE"
        self.envoie(requete)
    
    def stop(self):
        requete = "STOP"
        self.envoie(requete)


if __name__ == "__main__":
    client = Client("10.229.253.69", 1664)
    client.stop()


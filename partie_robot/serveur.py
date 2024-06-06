import socket
import mouvements
import capteurs

class Serveur():
    def __init__(self, port):
        self.ADRESSE = ""
        self.PORT = port
        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serveur.bind((self.ADRESSE, self.PORT))
        self.serveur.listen(10)
        self.moteur = mouvements.Mouvement()
        self.capteur = capteurs.Capteur()
    
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
        self.serveur.close()
    

    def recevoir_test(self):
        fin = False
        while fin == False:
            # Attente qu'un client se connecte
            client, adresse = self.serveur.accept()

            # Réception de la requete du client sous forme de bytes et transformation en string
            requete = client.recv(1024)
            if requete.decode() == "AVANCER":
                print("avancer")
            if requete.decode() == "RECULER":
                print("reculer")
            if requete.decode() == "GAUCHE":
                print("g")
            if requete.decode() == "DROITE":
                print("d")
            if requete.decode() == "LEVERBRAS":
                print("lb")
            if requete.decode() == "BAISSERBRAS":
                print("bb")
            if requete.decode() == "STOP":
                print("s")
            if requete.decode() == "X":
                print("x")
                fin = True

            # Déconnexion avec le client
            client.close()
            
        # Arrêt du serveur 
        self.serveur.close()


if __name__ == "__main__":
    s = Serveur(1664)
    s.recevoir_test()

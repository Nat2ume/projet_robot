"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
import sqlite3


# La classe
class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""

    def __init__(self, chemin_bdd):
        """Initialise la base de données

        Parameters:
            chemin_bdd (string) : chemin vers le fichier SQLite
        """
        self.chemin_bdd = chemin_bdd

    def recuperer_task(self,base):
        """Récupère des données

        Returns:
            (list of tuples) : liste des taches
        """
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            SELECT *
            FROM {base};"""
        resultat = curseur.execute(requete_sql)
        donnee = resultat.fetchall()
        connexion.close()
        return donnee
    
    def recuperer_task_demande(self,base,nom,date,pilote):
        """Récupère des données

        Returns:
            (list of tuples) : liste des taches
        """
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            SELECT * FROM '{base}' WHERE '{base}'.Nom = '{nom}' or '{base}'.Date = '{date}' or '{base}'.Pilote = '{pilote}';"""
        resultat = curseur.execute(requete_sql)
        donnee = resultat.fetchall()
        connexion.close()
        return donnee

# Mise au point de la classe Bdd seule
if __name__ == "__main__":
    # TODO : ajoutez le code pour tester et mettre au point votre classe Bdd
    test = Bdd("./bdd/nsium.sqlite")  
    print(test.recuperer_task('Nsium'))
"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
from flask import *
from bdd import*
from sqlite3 import*


# Création des objets Flask et Bdd
app = Flask(__name__)
bdd = Bdd("./bdd/nsium.sqlite")

@app.route("/")
def accueil():
    # Transmission pour affichage
    return render_template(
        "accueil.html",
    )

@app.route("/exploitation_de_donnees")
def Nsium():
    """Gère l'accueil des utilisateurs"""
    Base = bdd.recuperer_task('Nsium')
    print(Base)
    # Transmission pour affichage
    return render_template(
        "exploitation_de_donnees.html",base_nsium=Base)

@app.route("/exploitation_de_donnees")
def Obstacles():
    """Gère l'accueil des utilisateurs"""
    Base = bdd.recuperer_task('Obstacles')
    print(Base)
    # Transmission pour affichage
    return render_template(
        "exploitation_de_donnees.html",base_obstacles=Base)

@app.route("/exploitation_de_donnees")
def Recherche():
    """Gère l'accueil des utilisateurs"""
    Base = bdd.recuperer_task('Recherche')
    print(Base)
    # Transmission pour affichage
    return render_template(
        "exploitation_de_donnees.html",base_recherche=Base)

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)

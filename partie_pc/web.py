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
def exploitation():
    """Gère l'accueil des utilisateurs"""
    Base1 = bdd.recuperer_task('Nsium')
    Base2 = bdd.recuperer_task('Obstacles')
    Base3 = bdd.recuperer_task('Recherche')
    # Transmission pour affichage
    return render_template(
        "exploitation_de_donnees.html",base_nsium=Base1, base_obstacles=Base2,base_recherche=Base3)

@app.route("/exploitation")
def demande_exploitation():
    # Transmission pour affichage
    return render_template(
        "exploitation.html",
    )
@app.route("/exploitation", methods=["POST"])
def demande_bdd():
    base_donnee = request.form["bdd"]
    nom = request.form["nom"]
    pilote = request.form["pilote"]
    date = request.form["date"]
    Base = bdd.recuperer_task(base_donnee,nom,date,pilote)
    # Transmission pour affichage
    return render_template(
        "exploitation_de_donnees.html",base = Base)

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)

import sqlite3

# Fonction pour ajouter une ligne dans la base de données avec les coordonnées en cours
def ajouter_coordonnees(vel_x, vel_y, vel_z, time):
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()

    # Ajouter une nouvelle ligne à la table coordonates
    cursor.execute("INSERT INTO coordonates (vel_x, vel_y, vel_z, time) VALUES (?, ?, ?, ?)",
                   (vel_x, vel_y, vel_z, time))

    # Valider et enregistrer les modifications
    connect.commit()

    # Fermer la connexion
    connect.close()


# Fonction pour supprimer les lignes du tableau de la base de données
def supprimer_toutes_coordonnees():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()

    # Supprimer toutes les lignes de la table coordonates
    cursor.execute("DELETE FROM coordonates")

    # Valider et enregistrer les modifications
    connect.commit()

    # Fermer la connexion
    connect.close()



ajouter_coordonnees(1,1,1,0)
supprimer_toutes_coordonnees()





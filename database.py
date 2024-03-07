import sqlite3
import csv
import time
import keyboard
import pandas as pd

# Fonction pour ajouter une ligne dans la base de données avec les coordonnées en cours
def ecrire_db(id_vol, vel_x, vel_y, vel_z, time):
    try:
        # Ouvrir la connexion à la base de données
        connect = sqlite3.connect("test.db")
        cursor = connect.cursor()

        # Commencer une transaction
        cursor.execute("BEGIN")

        # Ajouter une nouvelle ligne à la table coordonates
        cursor.execute("INSERT INTO coordonates (id_vol, vel_x, vel_y, vel_z, time) VALUES (?, ?, ?, ?, ?)",
                       (id_vol, vel_x, vel_y, vel_z, time))

        # Valider et enregistrer les modifications
        connect.commit()
    except sqlite3.Error as e:
        print("Erreur SQLite:", e)
        # En cas d'erreur, annuler la transaction
        connect.rollback()
    finally:
        # Fermer la connexion dans le bloc 'finally' pour garantir qu'elle est toujours fermée
        if connect:
            connect.close()



def ecrire_csv(vel_x, vel_y, vel_z, time, nom_fichier='coord.csv'):
    # Ouvrir le fichier CSV pour ecrire les lignes
    with open(nom_fichier, mode='a', newline='') as fichier_csv:
        # Créer un objet writer pour écrire dans le fichier CSV
        writer = csv.writer(fichier_csv)

        # Écrire une nouvelle ligne avec les coordonnées actuelles
        writer.writerow([vel_x, vel_y, vel_z, time])

def suppr_csv(nom_fichier='coord.csv'):
    # Ouvrir le fichier CSV en mode écriture pour supprimer le contenu
    with open(nom_fichier, mode='w', newline='') as fichier_csv:
        # Créer un objet writer pour écrire dans le fichier CSV
        writer = csv.writer(fichier_csv)

        # Écrire une ligne vide pour effacer le contenu
        writer.writerow([])

def lire_csv(temps, nom_fichier='coord.csv'):
    # Ouvrir le fichier CSV en mode lecture
    with open(nom_fichier, mode='r', newline='') as fichier_csv:
        # Créer un objet reader pour lire le fichier CSV
        reader = csv.reader(fichier_csv)

        # Parcourir chaque ligne du fichier
        for ligne in reader:
            # Vérifier si la ligne contient des données
            if ligne:
                temps_ligne = float(ligne[3])  # index de la colonne temps

                # Si le temps correspond, retourner la ligne
                if temps_ligne == temps:
                    vel_x = float(ligne[0])  # index de la colonne vel_x
                    vel_y = float(ligne[1])  # index de la colonne vel_y
                    vel_z = float(ligne[2])  # index de la colonne vel_z
                    return vel_x, vel_y, vel_z

    # Si aucune ligne correspondante n'est trouvée, retourner None
    return None


# Fonction pour obtenir les coordonnées actuelles
def obtenir_coordonnees_actuelles():

    return 1, 1, 1  # pour l'instant on met sa vu que j'ai pas le robot


#Fonction pour obtenir l'id du dernier vol 
def obtenir_id_vol():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()

    # Vérifier si la table coordonates existe, sinon la créer
    cursor.execute("CREATE TABLE IF NOT EXISTS coordonates (id INTEGER PRIMARY KEY, id_vol INTEGER , vel_x INTEGER, vel_y INTEGER, vel_z INTEGER, time INTEGER )")

    cursor.execute("SELECT id_vol FROM coordonates ORDER BY id DESC LIMIT 1")
    id = cursor.fetchone()
    if id is not None: 
        id = id[0]
        connect.commit()
        connect.close()
        return id
    else:
        print("La table coordonates est vide.")
        connect.commit()
        connect.close()
        return 0
    

def nb_lignes_csv(nom_fichier='coord.csv'):
    try:
        # Charger le fichier CSV dans un DataFrame
        df = pd.read_csv(nom_fichier)
        
        # Renvoyer le nombre de lignes du DataFrame
        return len(df)
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return 0


##########  Teste des fonctions suivantes: ################
#   ecrire_csv()    : remplir une ligne d'un fichier csv (en local)
#   lire_csv()      : récupérer une ligne du fichier csv
#   obtenir_id_vol()    : récuperer le numéro de vol du dernier élement du tableau de la base de donnée

run = True
temp = 0
suppr_csv()

print('appuyer sur q pour arreter l enregistrement :')
# boucle d'enregistrement des données de vol en local
while True:
    if temp%1000 == 0 : 
        vel_x, vel_y, vel_z = obtenir_coordonnees_actuelles()
        ecrire_csv(vel_x, vel_y, vel_z, temp/1000)
    
    temp += 1  # Incrémenter le temps

    #sortie de la boucle si touche q pressee
    if keyboard.is_pressed('q'):
        print('q')
        break


# enregistrement des données locales sur la base de données
num_vol = obtenir_id_vol()
print('numéro de vol récupéré :', num_vol)
nb_lignes = nb_lignes_csv()
print("nb lignes à récupérer:", nb_lignes)
for i in range(nb_lignes):

    #recuperation des données de vol
    vel_x, vel_y, vel_z = lire_csv(i)
    print ('valeur récuperer: ',vel_x, vel_y, vel_z)

    #ecriture des données sur la base de donnee avec le numéro de vol suivant
    print('ecriture sur la base de donnée : ')
    ecrire_db(num_vol+1, vel_x, vel_y, vel_z, i)

    


# Projet : Drone Kit Mains Libres

Le drone est piloté à l'aide de la main, via à une caméra.
Et montre en temps réel, le déplacement du drone sur une map 3D.




## Documentation

[Hand Tracking by Murtaza's Workshop - Robotics and AI ](https://www.youtube.com/watch?v=NZde8Xt78Iw)

![Mediapipe](https://cdn.statically.io/img/media.geeksforgeeks.org/wp-content/uploads/20210802154942/HandLandmarks.png)

[SQLite tutorial](https://www.sqlitetutorial.net)

[Downloads - DB Browser for SQLite](https://sqlitebrowser.org/dl/)

![DB browers for SQLite](https://s.getwinpcsoft.com/screenshots/6080/6080575_1.jpg)
## FAQ

#### Question 1 : Comment faire fonctionner le drone ?

Ouvrire votre main sur le plan de la caméra

#### Question 2 : Comment stopper le robot ?

Fermer votre main sur le plan de la caméra

#### Question 3 : Comment avancer et reculer le drone ? 

Pour avancer : maintenez votre main en position ouverte et avance votre main sur le plan de la caméra

Pour reculer : maintenez votre main en position ouverte et reculer votre main sur le plan de la caméra

#### Question 4 : Comment piloter le drone de gauche à droite ? 

Bouger votre main (en position ouverte) de gauche à droite sur le plan de la caméra

#### Question 5 : Comment augmenter la hauteur du drone ?

Plier le majeur de votre main sur le plan de la caméra

#### Question 6 : Comment diminuer la hauteur du drone ? 

Plier l'index de votre main sur le plan de la caméra

#### Question 7 : Comment faire une rotation du drone ?

Faire une rotation de la main à horizontal sur le plan de la caméra

## Tracking drone

Le fichier Control_Drone_Main.py sert à piloter le drone en ayant un retour caméra sur l'écran afin de positionner sa main plus précisément et par conséquent, rendre le pilotage plus aisé.

Le fichier Control_Drone_Main2.py est un test d'implémentation de la sauvegarde de la base de donnée pendant et après un vol.

Le code analyse différentes parties de la main afin d'en déduire la position de celle-ci. Le drone suit ensuite les consignes données par la position de la main.

## Map 3D

La librairie "have_a_plot.py" permet d'afficher un rendu 3D en temps réel. Deux versions de cette librairie sont disponibles : 

"have_a_plot.py", qui se base sur les retours des capteurs du drone et est donc très proche de la réalité, mais ne fonctionne pas avec toutes les versions du drone. Sa fonction "refresh_coo()" ne demande aucun paramètre.

"have_a_plot_handV.py", qui se base sur la commande envoyée au drone pour afficher le 3D, et est donc moins proche de la réalité que "have_a_plot.py", mais fonctionne avec toutes les versions du drone. Sa fonction "refresh_coo()" prend la position x, y et z en paramètres.

Les étapes sont décrites en utlisant "have_a_plot_handV" à la place de "HPH". 

Etape 0 :
  Importer la librairy de votre choix : 
    ```
    import have_a_plot.py as HP
    ```
                ou
    ```import have_a_plot_handV.py as HPH"```
    
Etape 1 : 
  Initializer les variables internes avec : 
  ```HPH.init()```
  
Etape 2 :
  Lancer la vue 3D avec la fonction :
  ```have_a_plot.plot_the_3D()```

Etape 3 : 
  Actualizer les coordonées après chaque commande de mouvement :
  ```refresh_coo(x, y, z)```

Etape 4 :
  En fin de programme, fermer les processus : 
  ```HPH.end()```

![Image du fichier csv](Photo/plot_3D_result.png)


## Database
L'objectif de la base de donnée est de récuperer les données de vol du drone pour les stocker. On pourra par la suite les utiliser pour refaire le parcours sauvegardé.

La capture des données se fait tout d'abord en local, en utilisant un fichier .csv. Puis, une fois le vol terminé, les données sont stoquées dans la base de données.
Le fichier database.py permet de réaliser les tests unitaires des fonctions utilisant notre base de données (test.db).

Sur les images suivantes on voit les valeurs de test enregistré dans le fichier csv (en local) ainsi que dans la base de données.

![Image du fichier csv](Photo/image_donnee_local.png)
![Image de la table dans la base de donnée](Photo/image_donnee_sur_db.png)
## Running Tests

To run tests, run the following command

```bash
  python .\Control_Drone_Main
```


## Demonstration

![Untitled ‑ Made with FlexClip (1)](https://github.com/Jcosialls/drone/assets/119425942/cfd56459-cef8-4762-8180-af7dca581747)


## Futur optimisation
Utiliser des lunettes de réalité augmentée pour filmer nos mains. Cela permettrai d'avoir une caméra dynamique.
![](https://th.bing.com/th/id/R.7690812238d0a57a7decd48c57411962?rik=Q95wngrWbuX3ag&pid=ImgRaw&r=0) 

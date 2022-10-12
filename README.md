#### Participants:
* Alexandre Merle
* Yohann Pouillieute
# Notre Projet:
![logo tinder](https://boncoo.ovh/wp-content/uploads/2017/12/Logo-Tinder.svg_.png)
## Présentation du projet:
__1) Les difficultés:__

Tout d'abord on a voulu passer par panda afin de donner les caractérisques pour chaque personne mais ce fut un échec.
Nous avons aussi des bugs dans notre programme du type inversement de variable dans les class qui créait des bugs pour comparer les variables entre elles


__2)La réorganisation de notre plan de travail__

Après avoir lamentablement échoué avec panda nous nous sommes réorientés sur une méthode que l'on venait d'apprendre en cours:
* La POO (programmation orientée objet) 
-> celle ci nous a permis de pour définir nos personnages grâces aux class dans python
* Alexandre s'est occupé de créer la class Caracteristiques (celle qui définit les caractéristiques des personnage prédéfinit)
* Yohann s'est occupé de la class Profil (celle qui s'occupe du profil utilisateur)
* Yohann a ensuite rajouté la sous fonction presenter dans la class Caracteristiques permettant de présenter un personnage et les variables lui correspondant



Nos premières séances étaient donc dédiées à créer nos personnages. Les caractéristiques que nous avons donné sont le genre, le caractère, le signe astrologique, le genre musical, son orientation sexuel et enfin l'origine. Il y a une grande variabilité de caractéristique afin de couvrir toutes les possibles demandes d'un utilisateur. Après avoir défini chacun des personnages, nous avons réfléchi à la fonction match. Pour réaliser cette fonction complexe, nous avons décidé d'utiliser la récursivité et comparer les différences entre l'utilisateur et les personnages prédéfinis par la distance de hamming. Nous avons simultanément créé la fonction utilisateur avec input qui nous pose des questions qui correspondent aux caractéristiques que nous avons créé. L'utilisateur pourra alors matcher avec un ou plusieurs personnages qui leur ressemble en fonction des caractéristiques données.

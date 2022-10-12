#### Participants:
* Alexandre Merle
* Yohann Pouillieute
Temps pour réaliser le projet : environ 15h

# Notre Projet:
![logo tinder](https://boncoo.ovh/wp-content/uploads/2017/12/Logo-Tinder.svg_.png)
## Présentation du projet:
__1)Les difficultés:__

Tout d'abord on a voulu passer par panda afin de réaliser une IHM(interface homme-machine) mais ce fut un échec.
Les bugs nous ont fait perdre l'équivalent de 3h de travail après lesquelles nous avons décidé d'abandonné l'idée et de simplifier notre démarche.


__2)La réorganisation de notre plan de travail__

Après avoir lamentablement échoué avec panda nous nous sommes réorientés sur une méthode que l'on venait d'apprendre en cours:
* La POO (programmation orientée objet) 
-> celle ci nous a permis de pour définir nos personnages grâces aux class dans python
* Alexandre s'est occupé de créer la class Caracteristiques (celle qui définit les caractéristiques des personnages prédéfinit)
* Yohann s'est occupé de la class Profil (celle qui s'occupe du profil utilisateur)
* Nos premières séances étaient donc dédiées à créer nos personnages et de faire fonctionner correctement le code.
* Nous avons alors répartie le travail de manière à récupérer le temps perdu durant les 3 premières heures.

__3)Les caractéristiques possibles:__

Nous avons essayé de mettre un nombre de possibilités satisfaisante  à chaque fois pouvant représenter des caractéristiques souvent retrouvées. Nous sommes désolé si vous ne pouvez pas reproduire à la perfection votre profil :)
* l'age
* le genre (homme, femme)
* le caractère (passif, depressif, fetard, romantique)
* le signe astrologique( poisson, vierge, taureau, capricorne)
* le genre musical (rock,rap,electro, pop)
* son orientation sexuel (hetero, gay ,lesbienne)
* l'origine(la nationalité)

__4)Comment vérifier si une personne peut match avec le profil_utilisateur ?__

Après avoir défini chacun des personnages, nous avons réfléchi à la fonction match. Pour réaliser cette fonction complexe, nous avons décidé d'utiliser la __récursivité__ et comparer les différences entre l'utilisateur et les personnages prédéfinis grâce à la distance d'__Hamming__. Nous avons simultanément créé le profil utilisateur avec des __input__ qui nous pose des questions qui permettent de définir les caractéristiques que nous avons dans la __class Profil__. Nous ferons alors une présélection des personnes ressemblants sur certaines caractéristiques à notre profil_utilisateur

__5)Le choix final!__
Enfin 

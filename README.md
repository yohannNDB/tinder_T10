#### Participants:
* Alexandre Merle
* Yohann Pouillieute
Temps pour réaliser le projet : environ 15h

# Notre Projet:
![logo tinder](https://boncoo.ovh/wp-content/uploads/2017/12/Logo-Tinder.svg_.png)


## Présentation de Tinder:
- [wikidia de Tinder](https://fr.wikipedia.org/wiki/Tinder)
- [site de tinder](https://tinder.com/fr/about)


## Présentation du projet:
__1)Les difficultés:__

Pour commencer, nous avons voulu passer par panda afin de réaliser une IHM(interface homme-machine) mais ce fut un échec.
Les bugs nous ont fait perdre l'équivalent de 3h de travail après lesquelles nous avons décidé d'abandonné l'idée et de simplifier notre démarche.
![ihm de tinder](https://datingranking.net/wp-content/uploads/2021/04/tinder_6.jpg)

__2)La réorganisation de notre plan de travail__

Après avoir échoué avec panda nous nous sommes réorientés sur une méthode que l'on venait d'apprendre en cours et l'utilisation des lignes de commandes pour remplacer l'IHM:
* La POO (programmation orientée objet) 
-> celle ci nous a permis de définir nos personnages grâces aux class dans python
* Alexandre s'est occupé de créer la __class Caracteristiques__ (celle qui définit les caractéristiques des personnages prédéfinis)
```
class Caracteristiques():
    def __init__(self,age,genre,caractere, music_genre, astro, orientation, origine):
        self.age = age
        self.genre=genre
        self.caractere= caractere
        self.astro = astro
        self.music_genre = music_genre
        self.orientation_sex = orientation
        self.origine = origine
```
* Et de créer les personnages 
```
Jean_Pierre = Caracteristiques\
    (18,"homme","romantic","rap","taureau","gay","americain")

Magg_Azine = Caracteristiques\
     (87,"femme","agressif","rock","vierge","lesbienne","americain")
```
* Yohann s'est occupé de la __class Profil__(celle qui s'occupe du profil utilisateur)

```
class Profil():
    def __init__(self, age,genre,caractere, music_genre, astro, orientation, origine):
        self.Age = age
        self.Genre = genre
        self.Caractere= caractere
        self.Music_genre = music_genre
        self.Astro = astro
        self.Orientation_sex = orientation
        self.Origine = origine
```
* Et du profil utilisateur
```
Nom_prenom = Profil(\
                 check_for_age(), \

                 check_genre(),\

                 check_caractere(),\

                 check_style_musique_pref(),\

                 check_astro(),\

                 check_orientation_sex(),\

                 check_nationality())

```
* Nos premières séances étaient dédiées à créer nos personnages, et permettre a l'utilisateur de faire son profil.

```
#vérifie l'age de la personne qui veut s'inscrire
def check_for_age():
    while True :
        try:
            age = int(input("Entrer votre age: "))
        #si l'age n'est pas un entier,
        #la fonction redemande un autre age (ex: eight au lieu de 8)
        except ValueError:
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
        else:
            break
    #verifie sur l'utilisateur est majeur. si pas majeur alors le programme s'arrete
    if age >= 18:
        print("Vous avez l'âge légal pour entrer sur notre site de rencontre\n Veuillez créer votre profil: ")
        print(age)
        return age
    else:
        print("Vous n'avez pas l'âge légal pour entrer sur notre site de rencontre")
        exit()
* Nous avons répartie le travail de manière à récupérer le temps perdu durant les 3 premières heures.

```
__3)Les caractéristiques possibles:__

Nous avons essayé de mettre un nombre de possibilités satisfaisante  à chaque fois pouvant représenter des caractéristiques souvent retrouvées. Nous sommes désolé si vous ne pouvez pas reproduire à la perfection votre profil :)
* l'age(entre [18:99])-->-->```self.age = age```
* le genre (homme, femme)-->```self.genre=  genre```
* le caractère (passif, depressif, fetard, romantique)-->```self.caractere = caractere```
* le signe astrologique( poisson, vierge, taureau, capricorne)-->```self.astro = astro```
* le genre musical (rock,rap,electro, pop)-->```self.music_genre = music_genre```
* son orientation sexuel (hetero, gay ,lesbienne)-->```self.orientation = orientation```
* la nationalité(francais, americain, espagnol, marocain)-->```self.origine = origine```


__4)Comment vérifier si une personne peut matcher avec le profil_utilisateur ?__

Après avoir défini chacun des personnages, nous avons réfléchi à la fonction ```check_for_match```. Pour réaliser cette fonction complexe, nous avons décidé d'utiliser la __récursivité__ et comparer les différences entre l'utilisateur et les personnages prédéfinis grâce à la distance d'Hamming. Nous avons simultanément créé le profil utilisateur avec des ```input```qui nous pose des questions qui permettent de définir les caractéristiques que nous avons dans la ```class Profil```. Nous ferons alors une présélection des personnes ressemblants sur certaines caractéristiques à notre profil_utilisateur


```
 if distance_hamming_rec(A,a,cache=None) == 2:
    #Si orientation sexuelle différente c'est mort
    if distance_hamming_rec(B,b) == 0:
      possible_match.append(someone)
      personnages.remove(someone)
      check_for_match(Nom_prenom,personnages)
    else:
      not_possible_match.append(someone)
      personnages.remove(someone)
      check_for_match(Nom_prenom,personnages)
```



```
 if distance_hamming_rec(A,a,cache=None) == 2:
    #Si orientation sexuelle différente c'est mort
    if distance_hamming_rec(B,b) == 0:
      possible_match.append(someone)
      personnages.remove(someone)
      check_for_match(Nom_prenom,personnages)
    else:
      not_possible_match.append(someone)
      personnages.remove(someone)
      check_for_match(Nom_prenom,personnages)
```
__5)Le choix final!__
Enfin nous allons laisser le choix à l'utilisateur de match ou non avec certaines personnes. Il pourra soit match et la personne sera alors dans ses favoris ou alors il enlevera la personne de ses recommandés.


```
 if distance_hamming_rec(A,a,cache=None) == 2:
    #Si orientation sexuelle différente c'est mort
    if distance_hamming_rec(B,b) == 0:
      possible_match.append(someone)
      personnages.remove(someone)
      check_for_match(Nom_prenom,personnages)
    else:
      not_possible_match.append(someone)
      personnages.remove(someone)
      check_for_match(Nom_prenom,personnages)
```

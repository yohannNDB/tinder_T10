# Créé par merle, le 23/09/2022 en Python 3.7
class Caractéristiques():
    def __init__(self,genre,age,caractere, music_genre, astro, orientation, origine):
        self.age = age
        self.genre=genre
        self.caractere= caractere
        self.astro = astro
        self.music_genre = music_genre
        self.orientation_sex = orientation
        self.origine = origine
        def __changer_orientation_sexuelle_femme(self,nouvelle_orientation):
            if nouvelle_orientation == self.orientation_sex:
                print("C'est la même orientation ! :  " + str (nouvelle_orientation))
            else:
                self.orientation_sex = nouvelle_orientation
                print( "Votre nouvelle orientation: "+ str(nouvelle_orientation))
            return print(nouvelle_orientation)
'''
class Hommes():
    def __init__(self, age,caractere, music_genre, astro, orientation, origine):
        self.age = age
        self.caractere= caractere
        self.astro = astro
        self.music_genre = music_genre
        self.orientation_sex = orientation
        self.origine = origine
        def __changer_orientation_sexuelle_homme(self,nouvelle_orientation):
            if nouvelle_orientation == self.orientation_sex:
                print("C'est la même orientation ! :  " + str (nouvelle_orientation))
            else:
                self.orientation_sex = nouvelle_orientation
                print( "Votre nouvelle orientation: "+ str(nouvelle_orientation))
            return print(nouvelle_orientation)
'''

Jean_Kule= Caractéristiques("18","homme","romantic","rap","cancer","gay","americain")

Magg_Rosbeat = Caractéristiques("87","femme","agressif","rock","verge","lesbienne","americain")

Fany_Epi = Caractéristiques("45","femme","depressif","rap","gemaux","hétéro","marocain")

Faustine_MuletLaLibido= Caractéristiques("25","femme","fetard","pop","poisson","hétéro","espagnol")

Erwan_Erforsouhone= Caractéristiques("30","homme","passif","rock","capricorne","hétéro","marocain")

Eugène_Nocide= Caractéristiques("24","homme","agressif","électro","verge","hétéro", "francais")

Eva_Nouie = Caractéristiques("46","femme","romantic","pop","poisson","hétéro","français")

Frank_NStein = Caractéristiques("76","homme","agressif","rock","gemaux","gay","américain")

ElsaRose_LaPlante = Caractéristiques("22","femme","depressif","rap","capricorne","lesbienne","espagnol")

Laurent_Outan = Caractéristiques("35","homme","fetard","pop","poisson","hétéro","francais")

Scott_Che = Caractéristiques("26","homme","romantic","rap","cancer","hétéro","americain")

Jessica_Pote = Caractéristiques("19","femme","fetard","rock","gemaux","hétéro","espagnol")

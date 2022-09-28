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

class Profil():
    def __init__(self, age,genre,caractere, music_genre, astro, orientation, origine):
        self.Age = age
        self.Genre = genre
        self.Caractere= caractere
        self.Music_genre = music_genre
        self.Astro = astro
        self.Orientation_sex = orientation
        self.Origine = origine
        def __changer_orientation_sexuelle_homme(self,nouvelle_orientation):
            if nouvelle_orientation == self.orientation_sex:
                print("C'est la même orientation ! :  " + str (nouvelle_orientation))
            else:
                self.orientation_sex = nouvelle_orientation
                print( "Votre nouvelle orientation: "+ str(nouvelle_orientation))
            return print(nouvelle_orientation)


pretendant = [Jean_Kule, Magg_Rosbeat, Fany_Epi, Faustine_MuletLaLibido, Erwan_Erforsouhone, Eugène_Nocide, Eva_Nouie, Frank_NStein, ElsaRose_LaPlante, Laurent_Outan, Scott_Che, Jessica_Pote]
someone = random(pretendant)

Jean_Kule= Caractéristiques("18","homme","romantic","rap","cancer","gay","americain")

Magg_Rosbeat = Caractéristiques("87","femme","agressif","rock","verge","lesbienne","americain")

Fany_Epi = Caractéristiques("45","femme","depressif","rap","gemaux","hetero","marocain")

Faustine_MuletLaLibido= Caractéristiques("25","femme","fetard","pop","poisson","hetero","espagnol")

Erwan_Erforsouhone= Caractéristiques("30","homme","passif","rock","capricorne","hetero","marocain")

Eugène_Nocide= Caractéristiques("24","homme","agressif","électro","verge","hetero", "francais")

Eva_Nouie = Caractéristiques("46","femme","romantic","pop","poisson","hetero","français")

Frank_NStein = Caractéristiques("86","homme","agressif","rock","gemaux","gay","américain")

ElsaRose_LaPlante = Caractéristiques("22","femme","depressif","rap","capricorne","lesbienne","espagnol")

Laurent_Outan = Caractéristiques("35","homme","fetard","pop","poisson","hetero","francais")

Scott_Che = Caractéristiques("26","homme","romantic","rap","cancer","hetero","americain")

Jessica_Pote = Caractéristiques("19","femme","fetard","rock","gemaux","hetero","espagnol")





Nom_prenom = input("Entrer votre nom et votre prénom: ")
Nom_prenom = Profil(\
             input("Entrer votre âge: "),\

             input("Entrer votre genre h/f: "),\

             input("Entrer votre caractère\
                    romantic/agressif/depressif/fetard/passif: "),\

             input("Entrer votre style de musique préféré:\
                    rap/pop/electro/rock: "),\

             input("Entrer votre signe astrologique\
                    poisson/cancer/verge/gemaux/capricorne: "),\

             input("Entrer votre orientation sexuelle\
                    hetero/lesbienne/gay: "),\

             input("Entrer votre nationalité\
                    espagnol/americain/francais/marocain/autre: ")
             )

def distance_hamming_rec_cache_insecable(m1,m2,cache=None):
    if cache is None:
        cache = {}
    if (m1,m2) in cache:
        return cache[m1,m2]
    if max(len(m1), len(m2)) <= 2 or min(len(m1), len(m2)) <= 1:
        cache[m1,m2] = dist_hamming(m1,m2)
        return cache[m1,m2]
    else:
        i = len(m1)
        j = len(m2)
        d1 = distance_edition_rec_cache_insecable(m1[:i-2],m2[:j-1], cache) + dist_hamming(m1[i-2:], m2[j-1:])
        d2 = distance_edition_rec_cache_insecable(m1[:i-1],m2[:j-2], cache) + dist_hamming(m1[i-1:], m2[j-2:])
        d3 = distance_edition_rec_cache_insecable(m1[:i-1],m2[:j-1], cache) + dist_hamming(m1[i-1:], m2[j-1:])
        cache[m1,m2] = min(d1,d2,d3)
        return cache[m1,m2]


print(str(Nom_prenom))
possible_match = []
not_possible_match = []




def check_for_match(self,Nom_prenom,someone):
    if self.Age < 28 and self.age < 28:
        distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None)
        print(distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None))
        if distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None) == 2:
            pass
        else:
            distance_hamming_rec_cache_insecable(self.Orientation_sex,self.orientation_sex,cache=None)
            if distance_hamming_rec_cache_insecable(self.Orientation_sex,self.orientation_sex,cache=None) == 0:
                if distance_hamming_rec_cache_insecable(self.Origine,self.origine,cache=None) == 0:
                    return True
                elif distance_hamming_rec_cache_insecable(self.Origine,self.origine,cache=None) == 1:
                    pass

            else:
                pretendant.remove(someone)
                return False


    if self.Age > 28 and self.Age < 38 and self.age >28 and self.age < 38:
            distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None)
            print(distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None))
            if distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None) == 2:
                pass
            else:
                distance_hamming_rec_cache_insecable(self.Orientation_sex,self.orientation_sex,cache=None)
                if distance_hamming_rec_cache_insecable(self.Orientation_sex,self.orientation_sex,cache=None) == 0:
                    if distance_hamming_rec_cache_insecable(self.Origine,self.origine,cache=None) == 0:
                        return True
                    elif distance_hamming_rec_cache_insecable(self.Origine,self.origine,cache=None) == 1:
                        pass

                else:
                    pretendant.remove(someone)
                    return False

check_for_match()






def match(Nom_prenom):
    check_for_match(Nom_prenom,someone)
    if check_for_match == True:
        possible_match.append(someone)
        propose_match_to_profile()
    else:
        not_possible_match.append(someone)
        return




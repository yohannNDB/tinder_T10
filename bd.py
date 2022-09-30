# Cree par merle, le 23/09/2022 en Python 3.7
class Caracteristiques():
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




Jean_Kule = Caracteristiques\
            ("18","homme","romantic","rap","cancer","gay","americain")

Magg_Rosbeat = Caracteristiques\
            ("87","femme","agressif","rock","verge","lesbienne","americain")

Fany_Epi = Caracteristiques\
            ("45","femme","depressif","rap","gemaux","hetero","marocain")

Faustine_MuletLaLibido= Caracteristiques\
            ("25","femme","fetard","pop","poisson","hetero","espagnol")

Erwan_Erforsouhone= Caracteristiques\
            ("30","homme","passif","rock","capricorne","hetero","marocain")

Eugène_Nocide= Caracteristiques\
            ("24","homme","agressif","electro","verge","hetero", "francais")

Eva_Nouie = Caracteristiques\
            ("46","femme","romantic","pop","poisson","hetero","français")

Frank_NStein = Caracteristiques\
            ("86","homme","agressif","rock","gemaux","gay","americain")

ElsaRose_LaPlante = Caracteristiques\
            ("22","femme","depressif","rap","capricorne","lesbienne","espagnol")

Laurent_Outan = Caracteristiques\
            ("35","homme","fetard","pop","poisson","hetero","francais")

Scott_Che = Caracteristiques\
            ("26","homme","romantic","rap","cancer","hetero","americain")

Jessica_Pote = Caracteristiques\
            ("19","femme","fetard","rock","gemaux","hetero","espagnol")






Nom_prenom = input("Entrer votre nom et votre prenom: ")
Nom_prenom = Profil(\
             input("Entrer votre âge: "),\

             input("Entrer votre genre\
                    homme/femme: "),\

             input("Entrer votre caractère\
                    romantic/agressif/depressif/fetard/passif: "),\

             input("Entrer votre style de musique prefere:\
                    rap/pop/electro/rock: "),\

             input("Entrer votre signe astrologique\
                    poisson/cancer/verge/gemaux/capricorne: "),\

             input("Entrer votre orientation sexuelle\
                    hetero/lesbienne/gay: "),\

             input("Entrer votre nationalite\
                    espagnol/americain/francais/marocain/autre: ")
             )
def dist_hamming(m1,m2):
    d = abs(len(m1)-len(m2))
    for a,b in zip(m1,m2):
        if a != b :
            d += 1
    return d

def distance_hamming_rec(m1,m2,cache=None):
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
        d1 = distance_hamming_rec(m1[:i-2],m2[:j-1], cache) + dist_hamming(m1[i-2:], m2[j-1:])
        d2 = distance_hamming_rec(m1[:i-1],m2[:j-2], cache) + dist_hamming(m1[i-1:], m2[j-2:])
        d3 = distance_hamming_rec(m1[:i-1],m2[:j-1], cache) + dist_hamming(m1[i-1:], m2[j-1:])
        cache[m1,m2] = min(d1,d2,d3)
        return cache[m1,m2]


print(str(Nom_prenom))
possible_match = []
not_possible_match = []




def check_for_match(Nom_prenom,someone):
    A = Nom_prenom.genre
    a = someone.genre
    B = Nom_prenom.orientation_sex
    b = someone.orientation_sex
    C = Nom_prenom.origine
    c = someone.origine
    if personnage !=[]:

        #Verifie si meme tranche d'age
        if Nom_prenom.Age < 28 and someone.age < 28:
            #distance_hamming_rec(A,a,cache=None)
            #Si l'écart entre variable A et a ==2 cest donc un homme et une femme
            if distance_hamming_rec(A,a,cache=None) == 2:
                if distance_hamming_rec(B,b) == 0:
                    if distance_hamming_rec(C,c) > 5:
                        possible_match.append(someone)
                    else:
                        not_possible_match.append(someone)

            else:
                #distance_hamming_rec(self.Orientation_sex,self.orientation_sex,cache=None)
                if distance_hamming_rec(A,a,cache=None) == 0:
                    if distance_hamming_rec(self.Orientation_sex,self.orientation_sex,cache=None) == 0:
                        if distance_hamming_rec(self.Origine,self.origine,cache=None) == 0:
                            return True
                        elif distance_hamming_rec(self.Origine,self.origine,cache=None) == 1:
                            pass

                    else:
                        pretendant.remove(someone)
                        return False


        elif self.Age > 28 and self.Age < 38 and self.age >28 and self.age < 38:
            distance_hamming_rec(self.Genre,self.genre,cache=None)
            print(distance_hamming_rec(self.Genre,self.genre,cache=None))
            if distance_hamming_rec(self.Genre,self.genre,cache=None) == 2:
                distance_hamming_rec(self.Genre,self.genre,cache=None)
            else:
                distance_hamming_rec(self.Orientation_sex,self.orientation_sex,cache=None)
                if distance_hamming_rec(self.Orientation_sex,self.orientation_sex,cache=None) == 0:
                    if distance_hamming_rec(self.Origine,self.origine,cache=None) == 0:
                        possible_match.append(someone)
                    elif distance_hamming_rec(self.Origine,self.origine,cache=None) == 1:
                        pass
                else:
                    pretendant.remove(someone)

        else :
            pass
    else:
        print("Les personnes pouvant match avec vous sont: " +str(possible_match))
        return


distance_hamming_rec_cache_insecable(self.Genre,self.genre,cache=None)



def match(possible_match):





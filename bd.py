import random
from main import*



class Caracteristiques():
    def __init__(self,age,genre,caractere, music_genre, astro, orientation, origine):
        self.age = age
        self.genre=genre
        self.caractere= caractere
        self.astro = astro
        self.music_genre = music_genre
        self.orientation_sex = orientation
        self.origine = origine
    def presenter(self):
        texte = "Le profil de :" +str(possible-match[i]) + "\n"\
        "C'est un(e) "\
        +str(self.genre)\
        + " de " +str(self.age) \
        +" ans et il/elle est "\
        +str(self.caractere)+".\n"\
        +"Son style de musique préféré est le/la "\
        +str(self.music_genre)+".\n"\
        +"C'est un(e) "\
        +str(self.astro) \
        +". \n"\
        +"C'est un(e) "\
        +str(self.orientation_sex)\
        +" et il/elle est "\
        +str(self.origine)
        print(texte)


class Profil():
    def __init__(self, age,genre,caractere, music_genre, astro, orientation, origine):
        self.Age = age
        self.Genre = genre
        self.Caractere= caractere
        self.Music_genre = music_genre
        self.Astro = astro
        self.Orientation_sex = orientation
        self.Origine = origine




Jean_Pierre = Caracteristiques\
            (18,"homme","romantic","rap","taureau","gay","americain")

Magg_Azine = Caracteristiques\
            (87,"femme","agressif","rock","vierge","lesbienne","americain")

Fany_Epi = Caracteristiques\
            (45,"femme","depressif","rap","gemaux","hetero","marocain")

Faustine_Tirer= Caracteristiques\
            (25,"femme","fetard","pop","poisson","hetero","espagnol")

Erwan_Erforsouhone= Caracteristiques\
            (30,"homme","passif","rock","capricorne","hetero","marocain")

Eugène_Nocide= Caracteristiques\
            (24,"homme","agressif","electro","vierge","hetero", "francais")

Eva_Nouie = Caracteristiques\
            (46,"femme","romantic","pop","poisson","hetero","français")

Frank_NStein = Caracteristiques\
            (86,"homme","agressif","rock","gemaux","gay","americain")

ElsaRose_LaPlante = Caracteristiques\
            (22,"femme","depressif","rap","capricorne","lesbienne","espagnol")

Laurent_Outan = Caracteristiques\
            (35,"homme","fetard","pop","poisson","hetero","francais")

Scott_Che = Caracteristiques\
            (26,"homme","romantic","rap","taureau","hetero","americain")

Jessica_Noe = Caracteristiques\
            (19,"femme","fetard","rock","gemaux","hetero","espagnol")

Juliette_Suin = Caracteristiques\
            (18,"femme","agressif","pop","taureau","hetero", "francais")

personnages = [Jean_Pierre,\
               Jessica_Noe,\
               Magg_Azine,\
               Faustine_Tirer,\
               Scott_Che,\
               ElsaRose_LaPlante,\
               Laurent_Outan,\
               Frank_NStein,\
               Eva_Nouie,\
               Eugène_Nocide,\
               Erwan_Erforsouhone,\
               Fany_Epi,\
               Juliette_Suin]





Nom_prenom = input("Entrer votre nom et votre prenom: ")


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
## BESOIN fct qui vérifie si l'entrée utilisateur est une de celle que l'on attend

def check_genre():
    while True:
        try:
            genre = input("Entrer votre genre\
            homme/femme: ")
        except is_valid_genre(genre):
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
        else:
            break

    return genre




def is_valid_genre(genre):
    rep = True
    authorized_char =["femme","homme"]
    if char in genre not in authorized_char:
        rep = Falsef


def check_caractere():
    while True:
        try:
            caractere = input("Entrer votre caractère\
             romantic/agressif/depressif/fetard/passif: ")
        except ValueError:
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
        else:
            break
    return caractere


def check_style_musique_pref():
    while True:
        try:
            music_genre = input("Entrer votre style de musique prefere:\
             rap/pop/electro/rock: ")
        except ValueError:
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
        else:
            break
    return music_genre

def check_astro():
    while True:
        try:
            astro = input("Entrer votre signe astrologique:\
             poisson/taureau/verge/gemaux/capricorne: ")
        except ValueError:
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
            continue
        else:
            break
    return astro



def check_orientation_sex():
    while True:
        try:
            orientation_sex = input("Entrer votre orientation sexuelle\
             hetero/lesbienne/gay: ")
        except ValueError:
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
            continue
        else:
            break
    return orientation_sex


def check_nationality():
    while True:
        try:
            origine = input("Entrer votre nationalite\
             espagnol/americain/francais/marocain/autre: ")
        except ValueError:
            print("Ceci est une réponse non acceptée, entrez une valeur valide")
            continue
        else:
            break
    return origine



Nom_prenom = Profil(\
                 check_for_age(), \

                 check_genre(),\

                 check_caractere(),\

                 check_style_musique_pref(),\

                 check_astro(),\

                 check_orientation_sex(),\

                 check_nationality())


##Nom_prenom = Profil(25,"femme","passif","rap","poisson","gay","americain")
print(str(Nom_prenom.Age))

profil_utilisateur =\
    "Votre profil: \n"\
    "Vous êtes un(e) "\
    +str(Nom_prenom.Genre)\
    + " de " +str(Nom_prenom.Age) \
    +" ans et vous êtes plutôt "\
    +str(Nom_prenom.Caractere)+".\n"\
    +"Votre style de musique préféré est le/la "\
    +str(Nom_prenom.Music_genre)+".\n"\
    +"Vous êtes un "\
    +str(Nom_prenom.Astro) \
    +". \n"\
    +"Vous êtes "\
    +str(Nom_prenom.Orientation_sex)\
    +" et vous êtes "\
    +str(Nom_prenom.Origine)

print(profil_utilisateur)






definitiv_match = []
def main(possible_match):
    for i in range(len(possible_match)):
        possible_match[i].presenter()
        print("Voulez vous choisir ce profil comme un match ou un non match: ")
        choix = input("1 pour match, 2 pour non match")
        if choix ==1:
            definitiv_match.append(possible_match[i])
        else:
            possible_match.remove(possible_match[i])








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




possible_match = []
not_possible_match = []
def check_for_match(Nom_prenom,personnages):
    #condition d'arrêt
    if personnages == []:
        print("Les personnes pouvant match avec vous sont: " +str(possible_match))
        return main(possible_match)
    else:
        someone = random.choice(personnages)
        #definie le personnage comparé au profil uilisateur
        #variables que l'on utilisera
        A = Nom_prenom.Genre#genre de l'utilisateur
        a = someone.genre#genre du personnage
        B = Nom_prenom.Orientation_sex#orientation sexuelle utilisateur
        b = someone.orientation_sex#orientation sexuelle personnage
        C = Nom_prenom.Origine#origine utilisateur
        c = someone.origine#origine personnage
        utilisateur = Nom_prenom.Age
        mec = someone.age
        texte = str(Nom_prenom.Age),someone.age
        print(texte)
        print(type(mec))
        print(type(utilisateur))
        #Verifie si meme tranche d'age
        if utilisateur <= 28 and mec < 28:

            #Si l'écart entre variable A et a ==2 cest donc un homme et une femme
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


            else:
                #Sinon c'est soit un gay soit une lesbienne
                if distance_hamming_rec(A,a,cache=None) == 0:
                    if distance_hamming_rec(B,b,cache=None) == 0:
                        possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)
                    else:
                        not_possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)
                else:
                    not_possible_match.append(someone)
                    personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)



        elif Nom_prenom.Age >= 28 and Nom_prenom.Age <= 38\
        and someone.age >= 28 and someone.age <= 38:
            #Si l'écart entre variable A et a ==2 cest donc un homme et une femme
            if distance_hamming_rec(A,a,cache=None) == 2:
                #Si orientation sexuelle différente c'est mort
                if distance_hamming_rec(B,b) == 0:
                    possible_match.append(someone)
                    check_for_match(Nom_prenom,personnages)

                else:
                    not_possible_match.append(someone)
                    personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)

            else:
                #Sinon c'est soit un gay soit une lesbienne
                if distance_hamming_rec(A,a,cache=None) == 0:
                    if distance_hamming_rec(B,b,cache=None) == 0:
                        possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)

                    else:
                        not_possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)

                else:
                    not_possible_match.append(someone)
                    personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)



        #categorie d'age 38-55
        elif Nom_prenom.Age > 38 and Nom_prenom.Age <= 55 and someone.age > 38 and someone.age <= 55:


            #Si l'écart entre variable A et a ==2 cest donc un homme et une femme
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

            else:
                #Sinon c'est soit un gay soit une lesbienne
                if distance_hamming_rec(A,a,cache=None) == 0:
                    if distance_hamming_rec(B,b,cache=None) == 0:
                        possible_match.append(someone)
                        personnages.remove(personnages)
                        check_for_match(Nom_prenom,personnages)
                    else:
                        not_possible_match.append(someone)
                        personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)
                else:
                    not_possible_match.append(someone)
                    personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)



        else:
            #Si l'écart entre variable A et a ==2 cest donc un homme et une femme
            if distance_hamming_rec(A,a,cache = None) == 2:
                #Si orientation sexuelle différente c'est mort
                if distance_hamming_rec(B,b) == 0:
                    #si origine différente on considère qu'à cet age
                    #la personne ne fera pas le déplacement
                    if distance_hamming_rec(C,c,cache = None) == 0:
                        possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)

                    else:
                        not_possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)
                else:
                    not_possible_match.append(someone)
                    personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)

            else:
                #Sinon c'est soit un gay soit une lesbienne
                if distance_hamming_rec(A,a,cache = None) == 0:
                    #verifier si les deux sont GAY ou LESBIENNE
                    if distance_hamming_rec(B,b,cache = None) == 0:
                        possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)
                    else:
                        not_possible_match.append(someone)
                        personnages.remove(someone)
                        check_for_match(Nom_prenom,personnages)
                else:
                    not_possible_match.append(someone)
                    personnages.remove(someone)
                    check_for_match(Nom_prenom,personnages)




check_for_match(Nom_prenom,personnages)















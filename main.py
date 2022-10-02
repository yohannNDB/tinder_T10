from main import*
import random



personnages = [Jean_Pierre, \
               Jessica_Noe, \
               Magg_Azine, \
               Faustine_Tirer, \
               Scott_Che, \
               ElsaRose_LaPlante, \
               Laurent_Outan, \
               Frank_NStein, \
               Eva_Nouie, \
               Eugène_Nocide, \
               Erwan_Erforsouhone, \
               Fany_Epi, \
               Juliette_Suin]



someone =random.choice(personnages)

while True:
    try:
        validation = int(input("Validez vous votre profil? taper 1 si vous etes pret a commencer sinon taper 2 "))
        if validation ==1:
            check_for_match(Nom_prenom, someone)
    # si l'utilisateur ne tape pas un entier,
    # la fonction redemande une autre reponse (ex: oui au lieu de 1)
    except ValueError:
        print("Ceci est une réponse non acceptée, entrez une valeur valide")
        continue
    else:
        check_for_match(Nom_prenom,someone)

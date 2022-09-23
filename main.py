# Créé par pouillieut, le 23/09/2022 en Python 3.7
print("Bienvenue sur Tinder de Wish créer par Alexandre Merle et Yohann Pouillieute!\
       Nous vous invitons à créer votre profil!")
import bd
jeankule = Caracteristique()

genre = input("Êtes-vous un homme ou une femme? homme/femme")
nom_prenom = input("Pour commencer veuillez entrer votre Nom puis Prénom: ")
age = input("Veuillez entrer votre âge:")


def check_if_18(age):
    if age<18:
        print("Vous n'avez pas l'âge légal pour accéder a notre application")
        exit()
    else:
        print("Veuillez continuer la création de votre compte")

def filtres():
    if genre.get() == 1:
        genre = homme
    if genre.get() == 2:
        genre = femme

    if caractere.get() == 1:
        caractere =agressif
    if caractere.get() == 2:
        caractere = romantic
    if caractere.get() == 3:
        caractere = depressif
    if caractere.get() == 4:
        caractere = fetard
    if caractere.get() == 5:
        caractere = passif

    if signe_astro.get() == 1:
        astro = poisson
    if signe_astro.get() == 2:
        astro = cancer
    if signe_astro.get() == 3:
        astro = verge
    if signe_astro.get() == 4:
        astro = gemaux
    if signe_astro.get() == 5:
        astro = capricorne
    if genre_music.get() == 1:
        music_genre = rock
    if genre_music.get() == 2:
        music_genre = rap
    if genre_music.get() == 3:
        music_genre = pop
    if genre_music.get() == 4:
        music_genre = electro

    if orientation_sex.get() ==1:
        orientation = hetero
    if orientation_sex.get() == 2:
        orientation = lesbienne
    if orientation_sex.get() == 3:
        orientation = gay

    if origine.get() == 1:
        origine = americain
    if origine.get() == 2:
        origine = francais
    if origine.get() == 3:
        origine = espagnol
    if origine.get() == 4:
        origine = marocain
    if origine.get() == 5:
        origine = None

def CreateNewWindow():
# variables des cases cochées
    genre.set(0)
    caractere.set(0)
    signe_astro.set(0)
    genre_music.set(0)
    orientation_sex.set(0)
    origine.set(0)

#destruction de l'ancienne image de fond, du texte et du bouton
    canvas_pour_image.delete(ALL)

#création d'une nouvelle fenêtre avec une nouvelle taille
    window.title("Statistiques du Titanic")
    window.geometry("900x563")
    window.config(background = "#048B9A")
    window.iconbitmap("titanic.ico")
    window.resizable(width=False,height=False)

    canvas_pour_image.create_image(0,0,image = image_fond2,anchor='nw')
    canvas_pour_image.create_text(300,25,text="Vos informations",\
                                 font=("Roman",50, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,125,text="Votre genre :",\
                                 font=("Roman",25, "bold"),anchor='nw')
    canvas_pour_image.create_text(560,125,text="Votre caractere le plus fort: ",\
                                 font=("Roman",25, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,300,text="Votre genre de musique préféré: ",\
                                 font=("Roman",25, "bold"),anchor='nw')
    canvas_pour_image.create_text(560,300,text="Votre orientation sexuelle: ",\
                                 font=("Roman",25, "bold"),anchor='nw')



#caractéristiques des options du thème 1
    case_theme1_option1 = Radiobutton(window,text ='Homme',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=sex,value=1)
    case_theme1_option2 = Radiobutton(window,text ='Femme',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=sex,value=2)

#caractéristiques des options du thème 2
    case_theme2_option1 = Radiobutton(window,text ='agressif',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=1)

    case_theme2_option2 = Radiobutton(window,text ='romantic',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=classe,value=2)

    case_theme2_option3 = Radiobutton(window,text ='depressif',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=3)

    case_theme2_option4 = Radiobutton(window,text ='fetard',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=4)

    case_theme2_option5 = Radiobutton(window,text ='passif',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=5)



#caractéristiques des options du thème 3
    case_theme3_option1 = Radiobutton(window,text ='poisson',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=1)

    case_theme3_option2 = Radiobutton(window,text ='cancer',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=2)

    case_theme3_option3 = Radiobutton(window,text ='verge',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=3)

    case_theme3_option4 = Radiobutton(window,text ='gemaux',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=4)

    case_theme3_option5 = Radiobutton(window,text ='capricorne',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=5)

#caractéristiques des options du thème 4
    case_theme4_option1 = Radiobutton(window,text ='rock',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)

    case_theme4_option2 = Radiobutton(window,text ='rap',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)

    case_theme4_option3 = Radiobutton(window,text ='pop',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=3)

    case_theme4_option4 = Radiobutton(window,text ='electro',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=4)


    #caractéristiques des options du thème 5
    case_theme5_option1 = Radiobutton(window,text ='hetero',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)

    case_theme5_option2 = Radiobutton(window,text ='lesbienne',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)

    case_theme5_option3 = Radiobutton(window,text ='gay',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=3)


    #caractéristiques des options du thème 6
    case_theme6_option1 = Radiobutton(window,text ='americain',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)

    case_theme6_option2 = Radiobutton(window,text ='francais',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)


    case_theme6_option3 = Radiobutton(window,text ='espagnol',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=3)


    case_theme6_option4 = Radiobutton(window,text ='marocain',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=4)


    case_theme6_option5 = Radiobutton(window,text ='autre',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=5)




#caractéristiques du bouton "rechercher"
    button_rechercher = Button(window,text='Valider mon compte',bg='#FDD663',fg='black',\
                        font=("Roman",20),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_graphique)




#placements des options du theme 1
    case_theme1_option1.place(x=50,y=180)
    case_theme1_option2.place(x=50,y=220)

#placements des options du theme 2
    case_theme2_option1.place(x=580,y=180)
    case_theme2_option2.place(x=580,y=220)
    case_theme2_option3.place(x=580,y=260)

#placements des options du theme 3
    case_theme3_option1.place(x=50,y=360)
    case_theme3_option2.place(x=50,y=400)

#placements des options du theme 4
    case_theme4_option1.place(x=580,y=360)
    case_theme4_option2.place(x=580,y=400)

#placements des options du theme 5
    case_theme4_option1.place(x=580,y=360)
    case_theme4_option2.place(x=580,y=400)


#placements des options du theme 6
    case_theme4_option1.place(x=580,y=360)
    case_theme4_option2.place(x=580,y=400)
#placement du bouton "rechercher"
    button_rechercher.place(x=380,y=480)

# création du menu en haut
    menu_bar = Menu(window)
    menu_fill = Menu(menu_bar, tearoff=0)
    menu_fill.add_command(label="Choix des statistiques", command=CreateNewWindow)
    menu_fill.add_command(label="Quitter", command=Quitter)
    menu_bar.add_cascade(label="Fonction", menu=menu_fill)
    window.config(menu=menu_bar)



#fenêtre
window = Tk()

# variables des cases cochées
genre = IntVar(master= window, value= 0)
caractere = IntVar(master= window, value= 0)
signe_astro = IntVar(master= window, value= 0)
music_genre = IntVar(master= window, value= 0)
orientation = IntVar(master= window, value= 0)
origine = IntVar(master= window, value= 0)

#création de la fenêtre
window.title("Tinder")
window.geometry("710x444")
window.config(background = "#048B9A")
window.iconbitmap("titanic.ico")
window.resizable(width=False,height=False)

#image de fond
image_fond = PhotoImage(file = "fond_papier.gif")
image_fond2 = PhotoImage(file = "fond2.gif")

#image du bouton
image_bouton = PhotoImage(file="bouton_fond2.gif")

#création de l'image de fond et du Titre
canvas_pour_image = Canvas(window,width=1300,height=813, bg='white',bd=0,highlightthickness=0)
canvas_pour_image.create_image(0,0,image = image_fond,anchor='nw')
canvas_pour_image.create_text(20,150,text="Bienvenue dans l'applicationde statistiques du Titanic",\
                             font=("Script",35),anchor='nw')
canvas_pour_image.place(x=0,y=0)

menu_bar = Menu(window)
menu_fill = Menu(menu_bar, tearoff=0)
menu_fill.add_command(label="Quitter", command=Quitter)
menu_bar.add_cascade(label="Fonction", menu=menu_fill)
window.config(menu=menu_bar)

#boutton "commencer l'aventure" ansi que son placement dans la fenêtre
button1 = Button(window,image= image_bouton,borderwidth=0,\
                                highlightthickness=0,command=CreateNewWindow)
my_button1_window = canvas_pour_image.create_window\
                    (255,450/2,anchor = "nw",window=button1)

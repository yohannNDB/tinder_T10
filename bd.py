class Femmes():
    def __init__(self, age, music_genre, astro, orientation, origine):
        self.age = age
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

class Hommes():
    def __init__(self, age, music_genre, astro, orientation, origine):
        self.age = age
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



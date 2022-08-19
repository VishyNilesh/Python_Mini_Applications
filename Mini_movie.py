class Movie:
    def __init__(self,movie_name,hero_name,heroine_name):
        self.movie_name = movie_name
        self.hero_name = hero_name
        self.heroine_name = heroine_name
    def movie_info(self):
        print('Movie Name : ', self.movie_name)
        print('Hero  Name : ', self.hero_name)
        print('Heroine  Name : ', self.heroine_name)
        print()
l=[]
while True:
    choice = input('Do you want to add movie names ? : [Y|N] ')
    if choice.lower()=='n' or choice.lower()=='no':
        break
    else:
        title= input('Enter movie name : ')
        hero = input('Enter Hero name : ')
        heroine = input('Enter heroine name : ')
        m = Movie(title,hero,heroine)
        l.append(m)
for x in l:
    x.movie_info()
    print()
        
    


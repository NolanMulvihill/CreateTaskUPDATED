import random
champs = (("Aatrox", 'aatrox.jpeg', 'aatrox_silhouette.jpeg', 5000, 22.3, 4000), ("Ahri", 'ahri.jpeg', 'ahri_silhouette.jpeg', 300, 5.5, 145), ("Akali", 'akali.jpeg', 'akali_silhouette.jpeg', 19, 5.3, 110),
        ("Alistar", 'alistar.jpeg', 'alistar_silhouette.jpeg', 4500, 10.5, 1500), ("Amumu", 'amumu.jpeg', 'amumu_silhouette.jpeg', 5000, 3.7, 35), ("Annie", 'annie.jpeg', 'annie_silhouette.jpeg', 8, 4.2, 58), 
        ("Aphelios", 'aphelios.jpeg', 'aphelios_silhouette.jpeg', 18, 6, 130), ("Ashe", 'ashe.jpeg', 'ashe_silhouette.jpeg', 23, 5.9, 145), 
        ("Aurelion Sol", 'aurelion_sol.jpeg', 'aurelion_sol_silhouette.jpeg', 100000000000000000000000000, 1000000000000000000000000, 1000000000000000000000),("Azir", 'azir.jpeg', 'azir.jpeg', 3200, 8.5, 400), 
        ("Jinx", 'jinx.jpeg', 'jinx_silhouette.jpeg', 21, 5.3, 98), ("Mini Gnar", 'mini_gnar.jpeg' , 'mini_gnar_silhouette.jpeg', 2000, 2.5, 25), ("Mega Gnar", 'mega_gnar.jpeg', 'mega_gnar_silhouette.jpeg', 2000, 22, 6000))
class HigherOrLowerLOLMechanics:
    def __init__(self):
        #name, image, silloutee, age, height, and weight
        self._champs = champs
        
        self._category = 0 
        self._categories = ["Older or Younger", "Taller or Shorter", "Heavier or Lighter"]
        self._current_champ = 0
        self._next_champ = 1
        self._counter = 0
        self._high_score = 0

        

    def _create_category(self):
        new_comparison = random.randint(1,3)
        
        self._category = new_comparison + 2
        
        #print("Is " + self._champs[self._next_champ][0] + " " + self._categories[new_comparison - 1] + " than " +  self._champs[self._current_champ][0] + "?")
        
    
    def _create_next_champ(self):
        self._current_champ = self._next_champ
        
        while self._next_champ == self._current_champ:
            self._next_champ = random.randint(0, len(self._champs)-1)
        self._create_category()

    def _new_HorL(self):
        self._counter = 0
        
        self._current_champ = random.randint(0, len(self._champs)-1)
        while self._next_champ == self._current_champ:
            self._next_champ = random.randint(0, len(self._champs)-1)
        
        self._create_category()

    def _H_or_L(self, guess) -> bool:
        if guess == 1:
            if self._champs[self._next_champ][self._category] > self._champs[self._current_champ][self._category]:
                self._counter += 1
                if self._counter > self._high_score:
                    self._high_score = self._counter
                self._create_next_champ()
                return True
            else:
                self._counter = 0
                return False
        else:
            if guess == 0:
                if self._champs[self._next_champ][self._category] <= self._champs[self._current_champ][self._category]:
                    self._counter += 1
                    if self._counter > self._high_score:
                        self._high_score = self._counter
                    self._create_next_champ()
                    return True
                else:
                    self._counter = 0
                    return False
    def _current_champion_img(self) -> 'image file':
        return self._champs[self._current_champ][1]

    def _next_champion_img(self) -> 'image file':
        return self._champs[self._next_champ][1]

    def _get_category(self) -> str:
        return self._categories[self._category - 3]

    def _get_current_score(self) -> str:
        return str(self._counter)

    def _get_high_score(self) -> str:
        return str(self._high_score)


class WHOSTHATCHAMPIONMechanics:
    def __init__(self):
        self._champs = champs
        self._options = []
        self._answer = -1
        self._answer_placement = -1

    def _create_options(self):
        self._options = []
        self._answer = random.randint(0, len(self._champs)-1)
        self._answer_placement = random.randint(0, 3)

        for x in range(4):
            if x == self._answer_placement:
                self._options.append(self._champs[self._answer])
            else:
                filler = random.randint(0, len(self._champs)-1)
                while filler == self._answer or self._champs[filler] in self._options:
                    filler = random.randint(0, len(self._champs)-1)
                self._options.append(self._champs[filler])

    def _silhouette_img(self) -> 'image file':
        return self._champs[self._answer][2]

    def _champion_img(self) -> 'image file':
        return self._champs[self._answer][1]
    
    def _who_is_that(self, guess) -> bool:
        return guess == self._answer_placement

    def _new_WHOSTHATCHAMPION(self):
        self._create_options()

print('All champ data collected from https://dotesports.com/league-of-legends/news/how-tall-is-every-champion-in-league-of-legends')

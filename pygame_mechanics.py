import pygame
import game_mechanics

class GameDisplay:
    def __init__(self):
        self._running = True
        self._Higher_or_Lower = game_mechanics.HigherOrLowerLOLMechanics()
        self._WHOSTHATCHAMPION = game_mechanics.WHOSTHATCHAMPIONMechanics()
        self._game_running = False
        self._which_game = 1
        self._start = True
        self._guess = 0
        self._is_correct_champion = None
        
    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    break
                            
                if self._game_running:
                    if self._which_game == 1:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                if not self._Higher_or_Lower._H_or_L(1):
                                    self._game_running = False
                                    
                            if event.key == pygame.K_DOWN:
                                if not self._Higher_or_Lower._H_or_L(0):
                                    self._game_running = False
                    if self._which_game == 2:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                if self._guess == 0:
                                    self._guess = 1
                                else:
                                    if self._guess == 1:
                                        self._guess = 2
                                    else:
                                        if self._guess == 2:
                                            self._guess = 3
                                        else:
                                            if self._guess == 3:
                                                self._guess = 0
                            if event.key == pygame.K_UP:
                                self._is_correct_champion = self._WHOSTHATCHAMPION._who_is_that(self._guess)
                                self._game_running = False
                                
                                
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if self._which_game == 1:
                                self._Higher_or_Lower._new_HorL()
                                self._game_running = True
                                if self._start:
                                    self._start = False
                            if self._which_game == 2:
                                self._WHOSTHATCHAMPION._new_WHOSTHATCHAMPION()
                                self._game_running = True
                                self._guess = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            if self._which_game == 1:
                                self._which_game = 2
                                self._game_running = True
                                self._WHOSTHATCHAMPION._new_WHOSTHATCHAMPION()
                                self._guess = 0
                            else:
                                self._which_game = 1
                                self._start = True
                                self._game_running = False
                    

    def _display_Higher_or_Lower_Game(self) -> None:
        surface = pygame.display.get_surface()
        font = pygame.font.Font('freesansbold.ttf', 32)

        score = font.render(self._Higher_or_Lower._get_category(), True, (0,0,255), (255,255,255))
        score = pygame.transform.scale(score, (700, 100))
        surface.blit(score,(0,0))
        
        champ1 = pygame.image.load(f'champions/{self._Higher_or_Lower._current_champion_img()}')
        champ1 = pygame.transform.scale(champ1, (350, 600))
        surface.blit(champ1,(0,100))

        champ2 = pygame.image.load(f'champions/{self._Higher_or_Lower._next_champion_img()}')
        champ2 = pygame.transform.scale(champ2, (350, 600))
        surface.blit(champ2,(350,100))
        
        category = font.render(f'Current Score: {self._Higher_or_Lower._get_current_score()} High Score: {self._Higher_or_Lower._get_high_score()}', True, (0,0,255), (255,255,255))
        category = pygame.transform.scale(category, (surface.get_width(), 100))
        surface.blit(category,(0,700))
        
        pygame.display.flip()

    def _display_Higher_or_Lower_Start(self) -> None:
        surface = pygame.display.get_surface()

        font = pygame.font.Font('freesansbold.ttf', 32)

        title = font.render('Higher or Lower', True, (0,0,255), (255,255,255))
        title = pygame.transform.scale(title, (700, 100))
        surface.blit(title,(0,0))


        works = font.render('How the game works: Is the champion on the right is higher or lower in the given category on the top?', True, (255,0,0), (255,255,255))
        works = pygame.transform.scale(works, (700, 40))
        surface.blit(works,(0,100))


        higher = font.render('Click up arrow to guess higher', True, (0,175,0), (255,255,255))
        higher = pygame.transform.scale(higher, (700, 100))
        surface.blit(higher,(0,140))


        lower = font.render('Click down arrow to guess lower', True, (0,175,0), (255,255,255))
        lower = pygame.transform.scale(lower, (700, 100))
        surface.blit(lower,(0,240))
        

        start = font.render('Click left arrow to start the game', True, (0,175,0), (255,255,255))
        start = pygame.transform.scale(start, (700, 100))
        surface.blit(start,(0,340))

        change = font.render('Click right arrow to play \'WHO"S THAT CHAMPION!\'', True, (0,175,0), (255,255,255))
        change = pygame.transform.scale(change, (700, 100))
        surface.blit(change,(0,440))


        filler_font = pygame.font.Font('freesansbold.ttf', 150)
        filler = filler_font.render(':3', True, (0,0,0), (255,255,255))
        filler = pygame.transform.scale(filler, (700, 260))
        surface.blit(filler,(0,540))

        pygame.display.flip()

    def _display_Higher_or_Lower_End(self) -> None:
        surface = pygame.display.get_surface()

        font = pygame.font.Font('freesansbold.ttf', 32)
        
        title = font.render('GAME OVER', True, (0,0,255), (255,255,255))
        title = pygame.transform.scale(title, (700, 100))
        surface.blit(title,(0,0))

        start = font.render('Click left arrow to start new game', True, (0,175,0), (255,255,255))
        start = pygame.transform.scale(start, (700, 100))
        surface.blit(start,(0,100))

        change = font.render('Click right arrow to play \'WHO"S THAT CHAMPION!\'', True, (0,175,0), (255,255,255))
        change = pygame.transform.scale(change, (700, 100))
        surface.blit(change,(0,200))

        category = font.render(f'Current Score: {self._Higher_or_Lower._get_current_score()} High Score: {self._Higher_or_Lower._get_high_score()}', True, (0,0,255), (255,255,255))
        category = pygame.transform.scale(category, (700, 100))
        surface.blit(category,(0,700))


        filler_font = pygame.font.Font('freesansbold.ttf', 150)
        filler = filler_font.render(':3', True, (0,0,0), (255,255,255))
        filler = pygame.transform.scale(filler, (700, 400))
        surface.blit(filler,(0,300))

        pygame.display.flip()


    def _display_WHOS_THAT_CHAMPION_Game(self):
        surface = pygame.display.get_surface()
        
        champ = pygame.image.load(f'champions/{self._WHOSTHATCHAMPION._silhouette_img()}')
        champ = pygame.transform.scale(champ, (350, 600))
        surface.blit(champ,(0,100))

        font = pygame.font.Font('freesansbold.ttf', 32)

        title = font.render('WHO\'S THAT CHAMPION', True, (0,0,255), (255,255,255))
        title = pygame.transform.scale(title, (700, 100))
        surface.blit(title,(0,0))

        if self._guess == 0:
            color = (255, 215, 0)
        else:
            color = (255,255,255)
        
        option1 = font.render(f'1. {self._WHOSTHATCHAMPION._options[0][0]}', True, (0,0,255), color)
        option1 = pygame.transform.scale(option1, (350, 150))
        surface.blit(option1,(350,100))

        if self._guess == 1:
            color = (255, 215, 0)
        else:
            color = (255,255,255)

        option2 = font.render(f'2. {self._WHOSTHATCHAMPION._options[1][0]}', True, (0,0,255), color)
        option2 = pygame.transform.scale(option2, (350, 150))
        surface.blit(option2,(350,250))

        if self._guess == 2:
            color = (255, 215, 0)
        else:
            color = (255,255,255)

        option3 = font.render(f'3. {self._WHOSTHATCHAMPION._options[2][0]}', True, (0,0,255), color)
        option3 = pygame.transform.scale(option3, (350, 150))
        surface.blit(option3,(350,400))

        if self._guess == 3:
            color = (255, 215, 0)
        else:
            color = (255,255,255)

        option4 = font.render(f'4. {self._WHOSTHATCHAMPION._options[3][0]}', True, (0,0,255), color)
        option4 = pygame.transform.scale(option4, (350, 150))
        surface.blit(option4,(350,550))

        inputs = font.render('Use DOWN ARROW to change guess and UP ARROW to lock in', True, (0,0,255), (255, 255, 255))
        inputs = pygame.transform.scale(inputs, (700, 100))
        surface.blit(inputs,(0,700))
        
        pygame.display.flip()

    def _display_WHOS_THAT_CHAMPION_Result(self):
        surface = pygame.display.get_surface()
        
        champ = pygame.image.load(f'champions/{self._WHOSTHATCHAMPION._champion_img()}')
        champ = pygame.transform.scale(champ, (700, 600))
        surface.blit(champ,(0,100))

        font = pygame.font.Font('freesansbold.ttf', 32)

        if self._is_correct_champion:
            text = 'CORRECT'
        else:
            text = 'INCORRECT'

        result = font.render(text, True, (0,0,255), (255,255,255))
        result = pygame.transform.scale(result, (700,100))
        surface.blit(result,(0,0))

        play_again = font.render('Use LEFT ARROW to play again or RIGHT ARROW to play Higher or Lower', True, (0,0,255), (255,255,255))
        play_again = pygame.transform.scale(play_again, (700, 100))
        surface.blit(play_again,(0,700))

        pygame.display.flip()
        
    def _display(self):
        if self._which_game == 1:
            if self._game_running:
                self._display_Higher_or_Lower_Game()
            else:
                if self._start:
                    self._display_Higher_or_Lower_Start()
                else:
                    self._display_Higher_or_Lower_End()
        if self._which_game == 2:
            if self._game_running:
                self._display_WHOS_THAT_CHAMPION_Game()
            else:
                self._display_WHOS_THAT_CHAMPION_Result()
                        
                
        
    def run(self) -> None:
        pygame.init()
        pygame.display.set_mode((700,800))
        
        clock = pygame.time.Clock()
        while self._running:
            clock.tick(30)
            self._handle_events()
            self._display()
            

        pygame.quit()

    
print('All champion images gottten from: https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki')

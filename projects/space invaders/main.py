import pygame ,random , math
from pygame import mixer 

class SoundManager:
    def __init__(self):
        self.enable = True
        self.music_enable = True
        try:
            mixer.init()
            mixer.music.load("background.wav")
            mixer.music.play(-1)
        except pygame.error:
            print("No audio device found - running without sound.")
            self.enable = False

    def play_sound(self, filename):            
        if self.enable and self.music_enable:
            sound = mixer.Sound(filename)
            sound.play()
    
    def toggle_music(self):
        if not self.enable:
            return
        if self.music_enable:
            mixer.music.pause()
            self.music_enable = False
        else:
            mixer.music.unpause()
            self.music_enable = True    

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("player.png")
        self.x = x
        self.y = y
        self.speed = 200  # pixels per second
        self.change_x = 0

    def move_left(self):
        self.change_x = -self.speed
    
    def move_right(self):
        self.change_x = self.speed

    def stop(self):
        self.change_x = 0

    def update(self, delta_time):
        self.x += self.change_x * delta_time
        self.x = max(0, min(self.x, 736)) 

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Invader:
    def __init__(self, base_speed=50):
        self.image = pygame.image.load('invader1.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.base_speed = base_speed
        self.change_x = base_speed
        self.change_y = 40

    def update(self, delta_time):
        self.x += self.change_x * delta_time
        if self.x <= 0:
            self.change_x = abs(self.base_speed)
            self.y += abs(self.change_y)
        elif self.x >= 736:
            self.change_x = -abs(self.base_speed)
            self.y += self.change_y

    def respawn(self, new_speed = None):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        if new_speed is not None:
            self.base_speed = new_speed
            self.change_x = new_speed if self.change_x > 0 else -new_speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self):
        self.image = pygame.image.load("bullet.png")
        self.x = 0
        self.y = 480
        self.change_y = 450  # pixels per second
        self.state = "ready"

    def fire(self, x):
        if self.state == "ready":
            self.x = x
            self.y = 480
            self.state = "fire"

    def update(self, delta_time):
        if self.state == "fire":
            self.y -= self.change_y * delta_time
            if self.y <= 0:
                self.reset()

    def reset(self):
        self.y = 480
        self.state = "ready"

    def draw(self, surface):
        if self.state == "fire":
            surface.blit(self.image, (self.x + 16, self.y + 10))


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load("ufo.png"))
        self.background = pygame.image.load("background.jpg")
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.over_font = pygame.font.Font("freesansbold.ttf", 64)
        self.title_font = pygame.font.Font("freesansbold.ttf", 48)
        self.sound = SoundManager()


        self.reset_game()
        self.running = True
        self.state = "START"
        self.paused = False
        self.sfx_enabled = True

    def reset_game(self):
        self.player  = Player(370, 480)
        self.bullet = Bullet()
        self.invader_speed = 50
        self.invaders = [Invader(self.invader_speed) for _ in range(6)]
        self.score = 0
        self.level = 1
        self.next_level = 30 

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def show_level(self):   
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        self.screen.blit(level_text,(650, 10))
    
    def game_over(self):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        restart_text = self.font.render("Press R to Restart", True, (255, 255, 255))
        self.screen.blit(over_text, (200, 250))
        self.screen.blit(restart_text, (250, 320))

    def show_start_screen(self):
        title = self.title_font.render("SPACE INVADERS", True, (255, 255, 255))
        start_msg = self.font.render("Press any key to start", True, (255, 255, 255))
        self.screen.blit(title, (200, 200))
        self.screen.blit(start_msg, (230, 300))

    def show_paused(self):
        pause_text = self.title_font.render("PAUSED", True, (255, 255, 0))
        resume_text = self.font.render("Press P to resume", True, (255, 255, 255))
        self.screen.blit(pause_text, (300, 250))
        self.screen.blit(resume_text, (260, 320))        

    def check_collision(self, invader):
        distance = math.sqrt((invader.x - self.bullet.x) ** 2 + (invader.y - self.bullet.y) ** 2)
        return distance < 27

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if self.state == "START":
                        self.state = "PLAYING"
                
                    elif self.state == "PLAYING":
                            # pause toggle
                            if event.key == pygame.K_p:
                                self.paused = not self.paused

                            # toggle music
                            if event.key == pygame.K_m:
                                self.sound.toggle_music()

                            # toggle sound effects
                            if event.key == pygame.K_s:
                                self.sfx_enabled = not self.sfx_enabled

                            if not self.paused:    
                                if event.key == pygame.K_LEFT:
                                    self.player.move_left()
                                if event.key == pygame.K_RIGHT:
                                    self.player.move_right()
                                if event.key == pygame.K_SPACE and self.bullet.state == "ready":
                                    if self.sfx_enabled:
                                        self.sound.play_sound("laser.wav")
                                    self.bullet.fire(self.player.x)                                

                    elif self.state == "GAME_OVER":
                        if event.key == pygame.K_r:
                            self.reset_game()
                            self.state ="PLAYING"                        

                if event.type == pygame.KEYUP and self.state == "PLAYING":
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.player.stop()

            if self.state == "START":
                self.show_start_screen()

            elif self.state == "PLAYING":
                if not self.paused:                                   
                    self.player.update(delta_time)
                    self.bullet.update(delta_time)

                    for invader in self.invaders:
                        invader.update(delta_time)
                        if invader.y > 420:
                            for enemy in self.invaders:
                                enemy.y = 2000
                            self.state = "GAME_OVER"
                            break

                        if self.check_collision(invader):
                            self.bullet.reset()
                            self.score += 1
                            if self.sfx_enabled:
                                self.sound.play_sound("explosion.wav")
                            invader.respawn(self.invader_speed)
                        invader.draw(self.screen)

                    if self.score >= self.next_level:
                        self.level += 1
                        self.next_level += 30
                        self.invader_speed *= 1.3
                        for enemy in self.invaders:
                            enemy.base_speed = self.invader_speed
                            enemy.change_x = self.invader_speed if enemy.change_x > 0 else -self.invader_speed      
              

                    self.player.draw(self.screen)
                    self.bullet.draw(self.screen)
                    self.show_score()
                    self.show_level()
                else:
                    self.show_paused()

            elif self.state == "GAME_OVER":
                self.game_over()

            pygame.display.update()

if __name__ == "__main__":
    Game().run()
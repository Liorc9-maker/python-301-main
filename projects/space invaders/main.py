import pygame ,random , math
from pygame import mixer 

class SoundManager:
    def __init__(self):
        self.enable = True
        try:
            mixer.init()
            mixer.music.load("background.wav")
            mixer.music.play(-1)
        except pygame.error:
            print("No audio device found - running without sound.")
            self.enable = False

    def play_sound(self, filename):            
        if self.enable:
            sound = mixer.Sound(filename)
            sound.play()

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("player.png")
        self.x = x
        self.y = y
        self.speed = 0.7
        self.change_x = 0

    def move_left(self):
        self.change_x = - self.speed
    
    def move_right(self):
        self.change_x = self.speed

    def stop(self):
        self.change_x = 0

    def update(self):
        self.x += self.change_x
        self.x = max(0, min(self.x, 736)) 

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Invader:
    def __init__(self):
        self.image = pygame.image.load('invader1.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.change_x = 0.2
        self.change_y = 40

    def update(self):
        self.x += self.change_x
        if self.x <= 0:
            self.change_x = 0.2
            self.y += self.change_y
        elif self.x >= 736:
            self.change_x = -0.2
            self.y += self.change_y

    def respawn(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self):
        self.image = pygame.image.load("bullet.png")
        self.x = 0
        self.y = 480
        self.change_y = 2
        self.state = "ready"

    def fire(self, x):
        if self.state == "ready":
            self.x = x
            self.y = 480
            self.state = "fire"

    def update(self):
        if self.state == "fire":
            self.y -= self.change_y
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
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(pygame.image.load("ufo.png"))
        self.background = pygame.image.load("background.jpg")
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.over_font = pygame.font.Font("freesansbold.ttf", 64)
        self.sound = SoundManager()


        self.player  = Player(370, 480)
        self.bullet = Bullet()
        self.invaders = [Invader() for _ in range(6)]
        self.score = 0
        self.running = True

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def game_over(self):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(over_text, (200, 250))

    def check_collision(self, invader):
        distance = math.sqrt((invader.x - self.bullet.x) ** 2 + (invader.y - self.bullet.y) ** 2)
        return distance < 27

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    if event.key == pygame.K_SPACE:
                        if self.bullet.state == "ready":
                            self.sound.play_sound("laser.wav")
                            self.bullet.fire(self.player.x)

                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.player.stop()

            self.player.update()
            self.bullet.update()

            for invader in self.invaders:
                invader.update()
                if invader.y > 200:
                    for enemy in self.invaders:
                        enemy.y = 2000
                    self.game_over()
                    break
                if self.check_collision(invader):
                    self.bullet.reset()
                    self.score += 1
                    invader.respawn()
                invader.draw(self.screen)

            self.player.draw(self.screen)
            self.bullet.draw(self.screen)
            self.show_score()
            pygame.display.update()

if __name__ == "__main__":
    Game().run()
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed    
        if keys_pressed[K_s] and self.rect.y < H - 100:
            self.rect.y += self.speed
    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed    
        if keys_pressed[K_s] and self.rect.y < H - 100:
            self.rect.y += self.speed

W, H = 600, 500
window = display.set_mode((W, H))
display.set_caption('Пинг Понг')
back = (3, 252, 244)
window.fill(back)
display.set_caption("Пинг Понг")

clock = time.Clock()
FPS = 60

player = Player("shop_properly_file_2216_16298.png", 10, H//2, 25, 100, 10)
player2 = Player("shop_properly_file_2216_16297.png", W-35,H//2,25, 100, 10)
ball = GameSprite("treasure.png", W//2,H//2,50,50, 0)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
restart_game = font.render('PRESS SPACE FOR RESTART GAME!', True, (0, 0, 0))

speed_y = 3
speed_x = 3

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys

score1 = 0

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




display.update()
clock.tick(FPS)


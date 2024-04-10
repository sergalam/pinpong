from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


W, H = 600, 500
window = display.set_mode((W, H))
display.set_caption('Пинг Понг')
back = (3, 252, 244)
window.fill(back)

clock = time.Clock()
FPS = 60

score1 = 0

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        display.update()
        clock.tick(FPS)

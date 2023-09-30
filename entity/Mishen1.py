from setting import *
import random


class Mishen1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speed = None
        self.image = Mishenlevla1_png
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = random.randint(0, setting['w']), random.randint(0, setting['h'])

    def update(self):
        pass

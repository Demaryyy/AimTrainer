import os
import pygame as pg

setting = {
    'w': 1400,
    'h': 800,
    'title':'AimTrainer',
    'fps':120

}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder,'media')

Mishenlevla1_png = pg.image.load(os.path.join(media_folder,'Mishenlevla1.png'))

Mishenlevla2_png = pg.image.load(os.path.join(media_folder,'Mishenlevla2.png'))


FonLevla1_jpg = pg.image.load(os.path.join(media_folder,'FonLevla1.jpg'))

FonLevla2_jpg = pg.image.load(os.path.join(media_folder,'FonLevla2.jpg'))

clock = pg.time.Clock()
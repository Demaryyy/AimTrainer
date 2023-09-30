import random
from setting import *
from entity.Mishen1 import Mishen1
from entity.Mishen2 import Mishen2

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])

all_sprite = pg.sprite.Group()
mishen = Mishen1()
all_sprite.add(mishen)

font = pg.font.SysFont('Arial', 75)

TIMER = pg.USEREVENT + 1
pg.time.set_timer(TIMER, 1500)

score = 0


def repos():
    m = Mishen1()
    all_sprite.add(m)

def repos2():
    m2 = Mishen2()
    all_sprite.add(m2)

run = True

while run:

    clock.tick(setting['fps'])
    pg.display.flip()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if score > 15:
            screen.blit(FonLevla2_jpg, (0, 0))
        else:
            screen.blit(FonLevla1_jpg, (0, 0))

        for spr in all_sprite:
            if event.type == pg.MOUSEBUTTONDOWN:
                if spr.rect.collidepoint(event.pos):
                    spr.kill()
                    score += 1
                    if score < 15:
                        repos()
                    else:
                        repos2()

    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (setting['w'] / 2, 20))

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.flip()

pg.quit()

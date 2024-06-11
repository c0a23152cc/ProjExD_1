import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kou_img = pg.image.load("fig/3.png")
    kou_img = pg.transform.flip(kou_img,True, False)
    tmr = 0
    kou_rct = kou_img.get_rect() #硬貨トンのレクとを抽出
    kou_rct.center = 300,200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200
        x1=0
        y1=0
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img2, [-x+4800, 0])
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            y1=-1
        if key_lst[pg.K_DOWN]:
            y1=1
        if key_lst[pg.K_LEFT]:
            x1=-1
        if key_lst[pg.K_RIGHT]:
            x1=2
        kou_rct.move_ip((-1+x1,y1))
        screen.blit(kou_img,kou_rct) 
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
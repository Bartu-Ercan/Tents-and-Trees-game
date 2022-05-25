import pygame
import time

pygame.init()
surface = pygame.display.set_mode((600, 400))

WIDTH = 550
Background_color = (251,247,245)
Menu_Background_color = (0,0,0)
original_grid_element_color = (52, 31, 151)

def menu():
    pygame.init()
    menuwin = pygame.display.set_mode((WIDTH , WIDTH))
    pygame.display.set_caption("Main Menu")
    menuwin.fill(Menu_Background_color)

    quitbutton = pygame.image.load("quitpng.png")
    quitbutton = pygame.transform.scale(quitbutton , (275,61))

    playbutton = pygame.image.load("play.png")
    playbutton = pygame.transform.scale(playbutton , (275,61))

    rulesbutton = pygame.image.load("rules.jpg")
    rulesbutton = pygame.transform.scale(rulesbutton , (275,70))

    menuwin.blit(rulesbutton ,(137.5,200))
    menuwin.blit(playbutton , (137.5,100))
    menuwin.blit(quitbutton , (137.5,300))
    pygame.display.update()


    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 137.5 and mouse [0] < 412.5 and mouse [1] > 100 and mouse[1] < 161:
                    time.sleep(0.1)
                    main()
                elif mouse[0] > 137.5 and mouse [0] < 412.5 and mouse [1] > 200 and mouse[1] < 270:
                    time.sleep(0.1)
                    rules()
                elif mouse[0] > 137.5 and mouse [0] < 412.5 and mouse [1] > 300 and mouse[1] < 361:
                    time.sleep(0.1)
                    pygame.quit()


def rules():
    pygame.init()
    menuwin = pygame.display.set_mode((WIDTH , WIDTH))
    pygame.display.set_caption("Rules")
    menuwin.fill(Menu_Background_color)
    font = pygame.font.SysFont('Lemon Milk' , 14)
    quit_buton = pygame.image.load("quitpng.png")
    quit_buton = pygame.transform.scale(quit_buton ,(80,30))

    yazı = font.render("""Oyunda amaç,verilen zeminde rakamlardaki ipuçlarını kullanarak ve kurallara uyarak her ağaca bir çadır kurmak.""" , True , (255 , 0 , 0))
    yazı1 = font.render("""1-Her ağaca sadece bir çadır kurulmalı""" , True , (255 , 0 , 0))
    yazı2 = font.render("""2-Ağaca çadırlar yatay ve dikey kurulabilir.Çapraz çadır kurulamaz.""" , True , (255 , 0 , 0))
    yazı3 = font.render("""3-Rakamlar bize o sıra ve stündaki çadır sayısını ifade eder""" , True , (255 , 0 , 0))
    yazı4 = font.render("""4-Çadırlar yatay,dikey ve çapraz komşu olamaz""" , True , (255 , 0 , 0))
    menuwin.blit(yazı , (25,50))
    menuwin.blit(yazı1 , (25,100))
    menuwin.blit(yazı2 , (25,130))
    menuwin.blit(yazı3 , (25,160))
    menuwin.blit(yazı4 , (25,190))
    menuwin.blit(quit_buton , (450,500))
    pygame.display.update()


    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 450 and mouse [0] < 530 and mouse [1] > 500 and mouse[1] < 530:
                    time.sleep(0.1)
                    menu()

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH , WIDTH))
    pygame.display.set_caption("Çadır ve Ağaç")
    win.fill(Background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    myfont2 = pygame.font.SysFont('Lemon Milk' , 50)
    yazı0 = myfont.render("2" , True , (255 , 0 , 0))
    yazı1 = myfont.render("0" , True , (255 , 0 , 0))
    yazı2 = myfont.render("1" , True , (255 , 0 , 0))
    yazı3 = myfont.render("0" , True , (255 , 0 , 0))
    yazı4 = myfont.render("2" , True , (255 , 0 , 0))
    yazı5 = myfont.render("0" , True , (255 , 0 , 0))
    yazı6 = myfont.render("3" , True , (255 , 0 , 0))
    yazı7 = myfont.render("0" , True , (255 , 0 , 0))
    yazı8 = myfont.render("1" , True , (255 , 0 , 0))
    yazı9 = myfont.render("1" , True , (255 , 0 , 0))

    çadır = pygame.image.load("çadır.png")
    çadır = pygame.transform.scale(çadır , (40,40))

    ağaç = pygame.image.load("ağaç.png")
    ağaç = pygame.transform.scale(ağaç , (40,40))

    kazandınıztext = myfont2.render("Kazandınız" , True , (0, 255, 171))

    quit_buton = pygame.image.load("quit.png")
    quit_buton = pygame.transform.scale(quit_buton ,(75,41))

    restart_buton = pygame.image.load("reset.png")
    restart_buton = pygame.transform.scale(restart_buton ,(85,30))

    win.blit(restart_buton , (30,500))
    win.blit(quit_buton , (450,500))

    win.blit(yazı0 , (166,100))
    win.blit(yazı1 , (216,100))
    win.blit(yazı2 , (266,100))
    win.blit(yazı3 , (316,100))
    win.blit(yazı4 , (366,100))
    win.blit(yazı5 , (116,150))
    win.blit(yazı6 , (116,200))
    win.blit(yazı7 , (116,250))
    win.blit(yazı8 , (116,300))
    win.blit(yazı9 , (116,350))

    win.blit(ağaç , (355,156))
    win.blit(ağaç , (205,205))
    win.blit(ağaç , (155,255))
    win.blit(ağaç , (205,305))
    win.blit(ağaç , (305,355))

    for i in range(2,8):
        if (i == 2) or (i == 8):
            pygame.draw.line(win, (121, 218, 232) , (302 + 50 * i , 400) , (50 + 50 * i , 400) , 4 )
            pygame.draw.line(win, (121, 218, 232) , (400 , 302 + 50 * i) , (400 , 50 + 50 * i) , 4 )
            pygame.draw.line(win, (121, 218, 232) , (50 + 50 * i , 150) , (50 + 50 * i , 400) , 4 )
            pygame.draw.line(win, (121, 218, 232) , (150 , 50 + 50 * i) , (400 , 50 + 50 * i) , 4 )

        pygame.draw.line(win, (37, 37, 37) , (50 + 50 * i , 150) , (50 + 50 * i , 400) , 2 )
        pygame.draw.line(win, (37, 37, 37) , (150 , 50 + 50 * i) , (400 , 50 + 50 * i) , 2 )
    pygame.display.update()




    pygame.display.update()
    dogrusayısı = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 30 and mouse [0] < 115 and mouse [1] > 485 and mouse[1] < 530:
                    time.sleep(0.1)
                    main()
                if mouse[0] > 450 and mouse [0] < 525 and mouse [1] > 500 and mouse[1] < 541:
                    time.sleep(0.1)
                    menu()
                elif mouse[0] > 150 and mouse [0] < 200 and mouse [1] > 150 and mouse[1] < 200:
                    win.blit(çadır , (155,160))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 200 and mouse [0] < 250 and mouse [1] > 150 and mouse[1] < 200:
                    win.blit(çadır , (205,160))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 250 and mouse [0] < 300 and mouse [1] > 150 and mouse[1] < 200:
                    win.blit(çadır , (255,160))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 300 and mouse [0] < 350 and mouse [1] > 150 and mouse[1] < 200:
                    win.blit(çadır , (305,160))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()        
                elif mouse[0] > 150 and mouse [0] < 200 and mouse [1] > 200 and mouse[1] < 250:
                    win.blit(çadır , (155,210))
                    dogrusayısı = dogrusayısı + 1
                    pygame.display.update()        
                elif mouse[0] > 250 and mouse [0] < 300 and mouse [1] > 200 and mouse[1] < 250:
                    win.blit(çadır , (255,210))
                    dogrusayısı = dogrusayısı + 1
                    pygame.display.update() 
                elif mouse[0] > 300 and mouse [0] < 350 and mouse [1] > 200 and mouse[1] < 250:
                    win.blit(çadır , (305,210))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update() 
                elif mouse[0] > 350 and mouse [0] < 400 and mouse [1] > 200 and mouse[1] < 250:
                    win.blit(çadır , (355,210))
                    dogrusayısı = dogrusayısı + 1
                    pygame.display.update()
                elif mouse[0] > 200 and mouse [0] < 250 and mouse [1] > 250 and mouse[1] < 300:
                    win.blit(çadır , (205,260))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 250 and mouse [0] < 300 and mouse [1] > 250 and mouse[1] < 300:
                    win.blit(çadır , (255,260))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 300 and mouse [0] < 350 and mouse [1] > 350 and mouse[1] < 300:
                    win.blit(çadır , (305,260))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 350 and mouse [0] < 400 and mouse [1] > 250 and mouse[1] < 300:
                    win.blit(çadır , (355,260))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 300 and mouse [0] < 350 and mouse [1] > 250 and mouse[1] < 300:
                    win.blit(çadır , (305,260))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 150 and mouse [0] < 200 and mouse [1] > 300 and mouse[1] < 350:
                    win.blit(çadır , (155,310))
                    dogrusayısı = dogrusayısı + 1
                    pygame.display.update()
                elif mouse[0] > 250 and mouse [0] < 300 and mouse [1] > 300 and mouse[1] < 350:
                    win.blit(çadır , (255,310))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 300 and mouse [0] < 350 and mouse [1] > 300 and mouse[1] < 350:
                    win.blit(çadır , (300,310))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 350 and mouse [0] < 400 and mouse [1] > 300 and mouse[1] < 350:
                    win.blit(çadır , (355,310))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 150 and mouse [0] < 200 and mouse [1] > 300 and mouse[1] < 350:
                    win.blit(çadır , (155,310))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 150 and mouse [0] < 200 and mouse [1] > 350 and mouse[1] < 400:
                    win.blit(çadır , (155,360))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update() 
                elif mouse[0] > 200 and mouse [0] < 250 and mouse [1] > 350 and mouse[1] < 400:
                    win.blit(çadır , (205,360))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 250 and mouse [0] < 300 and mouse [1] > 350 and mouse[1] < 400:
                    win.blit(çadır , (255,360))
                    dogrusayısı = dogrusayısı - 1
                    pygame.display.update()
                elif mouse[0] > 350 and mouse [0] < 400 and mouse [1] > 350 and mouse[1] < 400:
                    win.blit(çadır , (355,360))
                    dogrusayısı = dogrusayısı + 1
                    pygame.display.update()
                if dogrusayısı == 5:
                    win.blit(kazandınıztext , (179,450))
                    pygame.display.update()
        pygame.display.update

menu()
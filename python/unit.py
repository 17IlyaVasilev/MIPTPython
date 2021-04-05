import pygame
import img


pygame.init()


class Lemon:
    num = 0
    lvl = 1
    cost_p = 5
    cost_l = 100
    money = 0.5
    autoclick = False
    cost_auto = 200
    player = pygame.Surface((900, 102))
    player.fill((0, 0, 0))
    number = pygame.Surface((400, 50))
    plus1 = pygame.Surface((300, 50))
    upgrade = pygame.Surface((300, 50))
    play = pygame.Surface((50, 50))
    play.fill((255, 255, 255))
    play.blit(img.Play, (0, 0))
    number.fill((255, 0, 0))
    plus1.fill((0, 255, 0))
    upgrade.fill((0, 0, 255))
    myfont = pygame.font.SysFont('monospace', 40)
    smallfont = pygame.font.SysFont('monospace', 20)
    autoc = pygame.Surface((100, 102))
    s1 = smallfont.render('Buy', 0, (0, 0, 0))
    s2 = smallfont.render('auto', 0, (0, 0, 0))
    s3 = smallfont.render('repeat', 0, (0, 0, 0))
    s4 = smallfont.render('cost', 0, (0, 0, 0))
    s5 = smallfont.render('($' + str(cost_auto) + ')', 0, (0, 0, 0))
    autoc.fill((0, 255, 255))
    autoc.blit(s1, (0, 0))
    autoc.blit(s2, (0, 20))
    autoc.blit(s3, (0, 40))
    autoc.blit(s4, (0, 60))
    autoc.blit(s5, (0, 80))
    player.blit(autoc, (800, 0))
    s = myfont.render('Amt: ' + str(num), 0, (0, 0, 0))
    number.blit(s, (0, 0))
    p = myfont.render('+', 0, (0, 0, 0))
    u = myfont.render('↑', 0, (0, 0, 0))
    splus1 = smallfont.render(' cost($' + str(cost_p) + ')', 0, (0, 0, 0))
    supgrade = smallfont.render(' cost($' + str(cost_l) + ')', 0, (0, 0, 0))
    plus1.blit(p, (0, 0))
    upgrade.blit(u, (0, 0))
    plus1.blit(splus1, (30, 10))
    upgrade.blit(supgrade, (30, 11))
    player.blit(img.Lemon, (0, 1))
    player.blit(number, (100, 1))
    player.blit(plus1, (500, 1))
    player.blit(upgrade, (500, 51))
    player.blit(play, (100, 51))
    player.set_colorkey((255, 255, 255))
    def time(self):
        return (10 / 2**(self.lvl-1))

class Gazeta:
    num = 0
    lvl = 1
    cost_p = 20
    cost_l = 400
    money = 2.0
    autoclick = False
    cost_auto = 800
    player = pygame.Surface((900, 102))
    player.fill((0, 0, 0))
    number = pygame.Surface((400, 50))
    plus1 = pygame.Surface((300, 50))
    upgrade = pygame.Surface((300, 50))
    play = pygame.Surface((50, 50))
    play.fill((255, 255, 255))
    play.blit(img.Play, (0, 0))
    player.blit(play, (100, 51))
    number.fill((255, 0, 0))
    plus1.fill((0, 255, 0))
    upgrade.fill((0, 0, 255))
    myfont = pygame.font.SysFont('monospace', 40)
    smallfont = pygame.font.SysFont('monospace', 20)
    autoc = pygame.Surface((100, 102))
    s1 = smallfont.render('Buy', 0, (0, 0, 0))
    s2 = smallfont.render('auto', 0, (0, 0, 0))
    s3 = smallfont.render('repeat', 0, (0, 0, 0))
    s4 = smallfont.render('cost', 0, (0, 0, 0))
    s5 = smallfont.render('($' + str(cost_auto) + ')', 0, (0, 0, 0))
    autoc.fill((0, 255, 255))
    autoc.blit(s1, (0, 0))
    autoc.blit(s2, (0, 20))
    autoc.blit(s3, (0, 40))
    autoc.blit(s4, (0, 60))
    autoc.blit(s5, (0, 80))
    player.blit(autoc, (800, 0))
    s = myfont.render('Amt: ' + str(num), 0, (0, 0, 0))
    number.blit(s, (0, 0))
    p = myfont.render('+', 0, (0, 0, 0))
    u = myfont.render('↑', 0, (0, 0, 0))
    splus1 = smallfont.render(' cost($' + str(cost_p) + ')', 0, (0, 0, 0))
    supgrade = smallfont.render(' cost($' + str(cost_l) + ')', 0, (0, 0, 0))
    plus1.blit(p, (0, 0))
    upgrade.blit(u, (0, 0))
    plus1.blit(splus1, (30, 10))
    upgrade.blit(supgrade, (30, 11))
    player.blit(img.Gazeta, (0, 1))
    player.blit(number, (100, 1))
    player.blit(plus1, (500, 1))
    player.blit(upgrade, (500, 51))
    player.set_colorkey((255, 255, 255))
    def time(self):
        return (20 / 2**(self.lvl-1))

class Coffee:
    num = 0
    lvl = 1
    cost_p = 50
    cost_l = 1000
    money = 5.0
    autoclick = False
    cost_auto = 2000
    player = pygame.Surface((900, 102))
    player.fill((0, 0, 0))
    number = pygame.Surface((400, 50))
    plus1 = pygame.Surface((300, 50))
    upgrade = pygame.Surface((300, 50))
    play = pygame.Surface((50, 50))
    play.fill((255, 255, 255))
    play.blit(img.Play, (0, 0))
    player.blit(play, (100, 51))
    number.fill((255, 0, 0))
    plus1.fill((0, 255, 0))
    upgrade.fill((0, 0, 255))
    myfont = pygame.font.SysFont('monospace', 40)
    smallfont = pygame.font.SysFont('monospace', 20)
    autoc = pygame.Surface((100, 102))
    s1 = smallfont.render('Buy', 0, (0, 0, 0))
    s2 = smallfont.render('auto', 0, (0, 0, 0))
    s3 = smallfont.render('repeat', 0, (0, 0, 0))
    s4 = smallfont.render('cost', 0, (0, 0, 0))
    s5 = smallfont.render('($' + str(cost_auto) + ')', 0, (0, 0, 0))
    autoc.fill((0, 255, 255))
    autoc.blit(s1, (0, 0))
    autoc.blit(s2, (0, 20))
    autoc.blit(s3, (0, 40))
    autoc.blit(s4, (0, 60))
    autoc.blit(s5, (0, 80))
    player.blit(autoc, (800, 0))
    s = myfont.render('Amt: ' + str(num), 0, (0, 0, 0))
    number.blit(s, (0, 0))
    p = myfont.render('+', 0, (0, 0, 0))
    u = myfont.render('↑', 0, (0, 0, 0))
    splus1 = smallfont.render(' cost($' + str(cost_p) + ')', 0, (0, 0, 0))
    supgrade = smallfont.render(' cost($' + str(cost_l) + ')', 0, (0, 0, 0))
    plus1.blit(p, (0, 0))
    upgrade.blit(u, (0, 0))
    plus1.blit(splus1, (30, 10))
    upgrade.blit(supgrade, (30, 11))
    player.blit(img.Coffee, (0, 1))
    player.blit(number, (100, 1))
    player.blit(plus1, (500, 1))
    player.blit(upgrade, (500, 51))
    player.set_colorkey((255, 255, 255))
    def time(self):
        return (30 / 2**(self.lvl-1))

class Pizza:
    num = 0
    lvl = 1
    cost_p = 1000
    cost_l = 40000
    money = 100.0
    autoclick = False
    cost_auto = 80000
    player = pygame.Surface((900, 102))
    player.fill((0, 0, 0))
    number = pygame.Surface((400, 50))
    plus1 = pygame.Surface((300, 50))
    upgrade = pygame.Surface((300, 50))
    play = pygame.Surface((50, 50))
    play.fill((255, 255, 255))
    play.blit(img.Play, (0, 0))
    player.blit(play, (100, 51))
    number.fill((255, 0, 0))
    plus1.fill((0, 255, 0))
    upgrade.fill((0, 0, 255))
    myfont = pygame.font.SysFont('monospace', 40)
    smallfont = pygame.font.SysFont('monospace', 20)
    autoc = pygame.Surface((100, 102))
    s1 = smallfont.render('Buy', 0, (0, 0, 0))
    s2 = smallfont.render('auto', 0, (0, 0, 0))
    s3 = smallfont.render('repeat', 0, (0, 0, 0))
    s4 = smallfont.render('cost', 0, (0, 0, 0))
    s5 = smallfont.render('($' + str(cost_auto) + ')', 0, (0, 0, 0))
    autoc.fill((0, 255, 255))
    autoc.blit(s1, (0, 0))
    autoc.blit(s2, (0, 20))
    autoc.blit(s3, (0, 40))
    autoc.blit(s4, (0, 60))
    autoc.blit(s5, (0, 80))
    player.blit(autoc, (800, 0))
    s = myfont.render('Amt: ' + str(num), 0, (0, 0, 0))
    number.blit(s, (0, 0))
    p = myfont.render('+', 0, (0, 0, 0))
    u = myfont.render('↑', 0, (0, 0, 0))
    splus1 = smallfont.render(' cost($' + str(cost_p) + ')', 0, (0, 0, 0))
    supgrade = smallfont.render(' cost($' + str(cost_l) + ')', 0, (0, 0, 0))
    plus1.blit(p, (0, 0))
    upgrade.blit(u, (0, 0))
    plus1.blit(splus1, (30, 10))
    upgrade.blit(supgrade, (30, 11))
    player.blit(img.Pizza, (0, 1))
    player.blit(number, (100, 1))
    player.blit(plus1, (500, 1))
    player.blit(upgrade, (500, 51))
    player.set_colorkey((255, 255, 255))
    def time(self):
        return (40 / 2**(self.lvl-1))

class Restaurant:
    num = 0
    lvl = 1
    cost_p = 5000
    cost_l = 200000
    money = 500.0
    autoclick = False
    cost_auto = 400000
    player = pygame.Surface((900, 102))
    player.fill((0, 0, 0))
    number = pygame.Surface((400, 50))
    plus1 = pygame.Surface((300, 50))
    upgrade = pygame.Surface((300, 50))
    play = pygame.Surface((50, 50))
    play.fill((255, 255, 255))
    play.blit(img.Play, (0, 0))
    player.blit(play, (100, 51))
    number.fill((255, 0, 0))
    plus1.fill((0, 255, 0))
    upgrade.fill((0, 0, 255))
    myfont = pygame.font.SysFont('monospace', 40)
    smallfont = pygame.font.SysFont('monospace', 20)
    autoc = pygame.Surface((100, 102))
    s1 = smallfont.render('Buy', 0, (0, 0, 0))
    s2 = smallfont.render('auto', 0, (0, 0, 0))
    s3 = smallfont.render('repeat', 0, (0, 0, 0))
    s4 = smallfont.render('cost', 0, (0, 0, 0))
    s5 = smallfont.render('($' + str(cost_auto) + ')', 0, (0, 0, 0))
    autoc.fill((0, 255, 255))
    autoc.blit(s1, (0, 0))
    autoc.blit(s2, (0, 20))
    autoc.blit(s3, (0, 40))
    autoc.blit(s4, (0, 60))
    autoc.blit(s5, (0, 80))
    player.blit(autoc, (800, 0))
    s = myfont.render('Amt: ' + str(num), 0, (0, 0, 0))
    number.blit(s, (0, 0))
    p = myfont.render('+', 0, (0, 0, 0))
    u = myfont.render('↑', 0, (0, 0, 0))
    splus1 = smallfont.render(' cost($' + str(cost_p) + ')', 0, (0, 0, 0))
    supgrade = smallfont.render(' cost($' + str(cost_l) + ')', 0, (0, 0, 0))
    plus1.blit(p, (0, 0))
    upgrade.blit(u, (0, 0))
    plus1.blit(splus1, (30, 10))
    upgrade.blit(supgrade, (30, 11))
    player.blit(img.Restaurant, (0, 1))
    player.blit(number, (100, 1))
    player.blit(plus1, (500, 1))
    player.blit(upgrade, (500, 51))
    player.set_colorkey((255, 255, 255))
    def time(self):
        return (50 / 2**(self.lvl-1))


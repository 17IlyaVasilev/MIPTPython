import var
import unit
import img
import pygame
import time


pygame.init()

def mouse(coord):
    if (coord[0] <= 800 and coord[0] >= 500):
        if (coord[1] <= 151 and coord[1] >= 101):
            if (var.Lemon.cost_p <= var.count_player_money):
                var.Lemon.num += 1
                var.count_player_money -= var.Lemon.cost_p
                var.Lemon.cost_p *= 1.1
        elif (coord[1] <= 202 and coord[1] >= 152):
            if (var.Lemon.cost_l <= var.count_player_money and var.Lemon.lvl < 5):
                var.Lemon.lvl += 1
                var.count_player_money -= var.Lemon.cost_l
                var.Lemon.cost_l *= 3
        elif (coord[1] <= 261 and coord[1] >= 211):
            if (var.Gazeta.cost_p <= var.count_player_money):
                var.Gazeta.num += 1
                var.count_player_money -= var.Gazeta.cost_p
                var.Gazeta.cost_p *= 1.1
        elif (coord[1] <= 312 and coord[1] >= 262):
            if (var.Gazeta.cost_l <= var.count_player_money and var.Gazeta.lvl < 5):
                var.Gazeta.lvl += 1
                var.count_player_money -= var.Gazeta.cost_l
                var.Gazeta.cost_l *= 3
        elif (coord[1] <= 371 and coord[1] >= 321):
            if (var.Coffee.cost_p <= var.count_player_money):
                var.Coffee.num += 1
                var.count_player_money -= var.Coffee.cost_p
                var.Coffee.cost_p *= 1.1
        elif (coord[1] <= 422 and coord[1] >= 372):
            if (var.Coffee.cost_l <= var.count_player_money and var.Coffee.lvl < 5):
                var.Coffee.lvl += 1
                var.count_player_money -= var.Coffee.cost_l
                var.Coffee.cost_l *= 3
        elif (coord[1] <= 481 and coord[1] >= 431):
            if (var.Pizza.cost_p <= var.count_player_money):
                var.Pizza.num += 1
                var.count_player_money -= var.Pizza.cost_p
                var.Pizza.cost_p *= 1.1
        elif (coord[1] <= 532 and coord[1] >= 482):
            if (var.Pizza.cost_l <= var.count_player_money and var.Pizza.lvl < 5):
                var.Pizza.lvl += 1
                var.count_player_money -= var.Pizza.cost_l
                var.Pizza.cost_l *= 3
        elif (coord[1] <= 591 and coord[1] >= 541):
            if (var.Restaurant.cost_p <= var.count_player_money):
                var.Restaurant.num += 1
                var.count_player_money -= var.Restaurant.cost_p
                var.Restaurant.cost_p *= 1.1
        elif (coord[1] <= 642 and coord[1] >= 592):
            if (var.Restaurant.cost_l <= var.count_player_money and var.Restaurant.lvl < 5):
                var.Restaurant.lvl += 1
                var.count_player_money -= var.Restaurant.cost_l
                var.Restaurant.cost_l *= 3


def changeMusic(coord):
    if (not var.flag):
        if (coord[0] >= 960 and coord[0] <= 1010):
            if (coord[1] >= 280 and coord[1] <= 330):
                if (var.Music1):
                    var.Music1 = False
                    img.Music1.stop()
                else:
                    var.sound = True
                    var.Music1 = True
                    img.Music1.play(-1)

                if (var.Music2):
                    var.Music2 = False
                    img.Music2.stop()

                if (var.Music3):
                    var.Music3 = False
                    img.Music3.stop()


            if (coord[1] >= 340 and coord[1] <= 390):
                if (var.Music1):
                    var.Music1 = False
                    img.Music1.stop()

                if (var.Music2):
                    var.Music2 = False
                    img.Music2.stop()
                else:
                    var.sound = True
                    var.Music2 = True
                    img.Music2.play(-1)

                if (var.Music3):
                    var.Music3 = False
                    img.Music3.stop()

            if (coord[1] >= 400 and coord[1] <= 450):
                if (var.Music1):
                    var.Music1 = False
                    img.Music1.stop()

                if (var.Music2):
                    var.Music2 = False
                    img.Music2.stop()

                if (var.Music3):
                    var.Music3 = False
                    img.Music3.stop()
                else:
                    var.sound = True
                    var.Music3 = True
                    img.Music3.play(-1)


def updateRecords():
    if (var.place == 10):
        var.m10 = var.count_player_money
        if (var.count_player_money > var.m9):
            var.place -= 1
            var.m10 = var.m9
            var.m9 = var.count_player_money
            var.n10 = var.n9
            var.n9 = 'You'
    if (var.place == 9):
        var.m9 = var.count_player_money
        if (var.count_player_money > var.m8):
            var.place -= 1
            var.m9 = var.m8
            var.m8 = var.count_player_money
            var.n9 = var.n8
            var.n8 = 'You'
    if (var.place == 8):
        var.m8 = var.count_player_money
        if (var.count_player_money > var.m7):
            var.place -= 1
            var.m8 = var.m7
            var.m7 = var.count_player_money
            var.n8 = var.n7
            var.n7 = 'You'
    if (var.place == 7):
        var.m7 = var.count_player_money
        if (var.count_player_money > var.m6):
            var.place -= 1
            var.m7 = var.m6
            var.m6 = var.count_player_money
            var.n7 = var.n6
            var.n6 = 'You'
    if (var.place == 6):
        var.m6 = var.count_player_money
        if (var.count_player_money > var.m5):
            var.place -= 1
            var.m6 = var.m5
            var.m5 = var.count_player_money
            var.n6 = var.n5
            var.n5 = 'You'
    if (var.place == 5):
        var.m5 = var.count_player_money
        if (var.count_player_money > var.m4):
            var.place -= 1
            var.m5 = var.m4
            var.m4 = var.count_player_money
            var.n5 = var.n4
            var.n4 = 'You'
    if (var.place == 4):
        var.m4 = var.count_player_money
        if (var.count_player_money > var.m3):
            var.place -= 1
            var.m4 = var.m3
            var.m3 = var.count_player_money
            var.n4 = var.n3
            var.n3 = 'You'
    if (var.place == 3):
        var.m3 = var.count_player_money
        if (var.count_player_money > var.m2):
            var.place -= 1
            var.m3 = var.m2
            var.m2 = var.count_player_money
            var.n3 = var.n2
            var.n2 = 'You'
    if (var.place == 2):
        var.m2 = var.count_player_money
        if (var.count_player_money > var.m1):
            var.place -= 1
            var.m2 = var.m1
            var.m1 = var.count_player_money
            var.n2 = var.n1
            var.n1 = 'You'
    if (var.place == 1):
        var.m1 = var.count_player_money
        if (var.count_player_money < var.m2):
            var.place += 1
            var.m1 = var.m2
            var.m2 = var.count_player_money
            var.n1 = var.n2
            var.n2 = 'You'
    if (var.place == 2):
        var.m2 = var.count_player_money
        if (var.count_player_money < var.m3):
            var.place += 1
            var.m2 = var.m3
            var.m3 = var.count_player_money
            var.n2 = var.n3
            var.n3 = 'You'
    if (var.place == 3):
        var.m3 = var.count_player_money
        if (var.count_player_money < var.m4):
            var.place += 1
            var.m3 = var.m4
            var.m4 = var.count_player_money
            var.n3 = var.n4
            var.n4 = 'You'
    if (var.place == 4):
        var.m4 = var.count_player_money
        if (var.count_player_money < var.m5):
            var.place += 1
            var.m4 = var.m5
            var.m5 = var.count_player_money
            var.n4 = var.n5
            var.n5 = 'You'
    if (var.place == 5):
        var.m5 = var.count_player_money
        if (var.count_player_money < var.m6):
            var.place += 1
            var.m5 = var.m6
            var.m6 = var.count_player_money
            var.n5 = var.n6
            var.n6 = 'You'
    if (var.place == 6):
        var.m6 = var.count_player_money
        if (var.count_player_money < var.m7):
            var.place += 1
            var.m6 = var.m7
            var.m7 = var.count_player_money
            var.n6 = var.n7
            var.n7 = 'You'
    if (var.place == 7):
        var.m7 = var.count_player_money
        if (var.count_player_money < var.m8):
            var.place += 1
            var.m7 = var.m8
            var.m8 = var.count_player_money
            var.n7 = var.n8
            var.n8 = 'You'
    if (var.place == 8):
        var.m8 = var.count_player_money
        if (var.count_player_money < var.m9):
            var.place += 1
            var.m8 = var.m9
            var.m9 = var.count_player_money
            var.n8 = var.n9
            var.n9 = 'You'
    if (var.place == 9):
        var.m9 = var.count_player_money
        if (var.count_player_money < var.m10):
            var.place += 1
            var.m9 = var.m10
            var.m10 = var.count_player_money
            var.n9 = var.n10
            var.n10 = 'You'


    if (var.place == 1):
        var.s1 = var.smallfont.render(var.n1 + ' $' + "{0:.2f}".format(var.m1), 0, (255, 255, 255))
    else:
        var.s1 = var.smallfont.render(var.n1 + ' $' + "{0:.2f}".format(var.m1), 0, (0, 0, 0))

    if (var.place == 2):
        var.s2 = var.smallfont.render(var.n2 + ' $' + "{0:.2f}".format(var.m2), 0, (255, 255, 255))
    else:
        var.s2 = var.smallfont.render(var.n2 + ' $' + "{0:.2f}".format(var.m2), 0, (0, 0, 0))

    if (var.place == 3):
        var.s3 = var.smallfont.render(var.n3 + ' $' + "{0:.2f}".format(var.m3), 0, (255, 255, 255))
    else:
        var.s3 = var.smallfont.render(var.n3 + ' $' + "{0:.2f}".format(var.m3), 0, (0, 0, 0))

    if (var.place == 4):
        var.s4 = var.smallfont.render(var.n4 + ' $' + "{0:.2f}".format(var.m4), 0, (255, 255, 255))
    else:
        var.s4 = var.smallfont.render(var.n4 + ' $' + "{0:.2f}".format(var.m4), 0, (0, 0, 0))

    if (var.place == 5):
        var.s5 = var.smallfont.render(var.n5 + ' $' + "{0:.2f}".format(var.m5), 0, (255, 255, 255))
    else:
        var.s5 = var.smallfont.render(var.n5 + ' $' + "{0:.2f}".format(var.m5), 0, (0, 0, 0))

    if (var.place == 6):
        var.s6 = var.smallfont.render(var.n6 + ' $' + "{0:.2f}".format(var.m6), 0, (255, 255, 255))
    else:
        var.s6 = var.smallfont.render(var.n6 + ' $' + "{0:.2f}".format(var.m6), 0, (0, 0, 0))

    if (var.place == 7):
        var.s7 = var.smallfont.render(var.n7 + ' $' + "{0:.2f}".format(var.m7), 0, (255, 255, 255))
    else:
        var.s7 = var.smallfont.render(var.n7 + ' $' + "{0:.2f}".format(var.m7), 0, (0, 0, 0))

    if (var.place == 8):
        var.s8 = var.smallfont.render(var.n8 + ' $' + "{0:.2f}".format(var.m8), 0, (255, 255, 255))
    else:
        var.s8 = var.smallfont.render(var.n8 + ' $' + "{0:.2f}".format(var.m8), 0, (0, 0, 0))

    if (var.place == 9):
        var.s9 = var.smallfont.render(var.n9 + ' $' + "{0:.2f}".format(var.m9), 0, (255, 255, 255))
    else:
        var.s9 = var.smallfont.render(var.n9 + ' $' + "{0:.2f}".format(var.m9), 0, (0, 0, 0))

    if (var.place == 10):
        var.s10 = var.smallfont.render(var.n10 + ' $' + "{0:.2f}".format(var.m10), 0, (255, 255, 255))
    else:
        var.s10 = var.smallfont.render(var.n10 + ' $' + "{0:.2f}".format(var.m10), 0, (0, 0, 0))

def flagChange(coord):
    if (var.flag):
        if (coord[0] >= 1105 and coord[0] <= 1280 and coord[1] >= 150 and coord[1] <= 200):
            var.flag = False
            var.Records.blit(img.Menu1, (0, 0))
            var.Settings.blit(img.Menu2, (0, 0))
            var.Records.blit(var.srecords, (0, 0))
            var.Settings.blit(var.ssettings, (0, 0))
    else:
        if (coord[0] >= 930 and coord[0] <= 1105 and coord[1] >= 150 and coord[1] <= 200):
            var.flag = True
            var.Records.blit(img.Menu2, (0, 0))
            var.Settings.blit(img.Menu1, (0, 0))
            var.Records.blit(var.srecords, (0, 0))
            var.Settings.blit(var.ssettings, (0, 0))

def soundChange(coord):
    if (not var.flag):
        if (coord[0] >= 1160 and coord[0] <= 1210 and coord[1] >= 220 and coord[1] <= 270):
            if (var.sound):
                var.sound = False
                var.Music1 = False
                var.Music2 = False
                var.Music3 = False
                img.Music1.stop()
                img.Music2.stop()
                img.Music3.stop()
                var.Sound.blit(img.SoundOff, (0, 0))
            else:
                var.sound = True
                var.Sound.blit(img.SoundOn, (0, 0))

def updateMusic():
    if (var.sound):
        var.Sound.blit(img.SoundOn, (0, 0))
    else:
        var.Sound.blit(img.SoundOff, (0, 0))

    if (var.Music1):
        var.Music_play1.blit(img.Pause, (0, 0))
    else:
        var.Music_play1.blit(img.Play, (0, 0))

    if (var.Music2):
        var.Music_play2.blit(img.Pause, (0, 0))
    else:
        var.Music_play2.blit(img.Play, (0, 0))

    if (var.Music3):
        var.Music_play3.blit(img.Pause, (0, 0))
    else:
        var.Music_play3.blit(img.Play, (0, 0))


def updateMenu():
    var.Menu.blit(img.Menu, (0, 0))
    var.Money.fill((0, 255, 0))
    updateRecords()
    money = var.myfont.render('$' + "{0:.2f}".format(var.count_player_money), 0, (0, 0, 0))
    var.Money.blit(money, (0, 0))
    var.Menu.blit(var.Money, (0, 0))
    var.Menu.blit(var.Records, (0, 50))
    var.Menu.blit(var.Settings, (175, 50))

    if (var.flag):
        var.Menu.blit(var.s1, (0, 110))
        var.Menu.blit(var.s2, (0, 150))
        var.Menu.blit(var.s3, (0, 190))
        var.Menu.blit(var.s4, (0, 230))
        var.Menu.blit(var.s5, (0, 270))
        var.Menu.blit(var.s6, (0, 310))
        var.Menu.blit(var.s7, (0, 350))
        var.Menu.blit(var.s8, (0, 390))
        var.Menu.blit(var.s9, (0, 430))
        var.Menu.blit(var.s10, (0, 470))
    else:
        updateMusic()
        var.Menu.blit(var.Music, (30, 120))
        var.Menu.blit(var.Music_play1, (30, 180))
        var.Menu.blit(var.Music_play2, (30, 240))
        var.Menu.blit(var.Music_play3, (30, 300))
        var.Menu.blit(var.Sound, (230, 120))



def updateLemon():
    if (var.Lemon.autoclick):
        var.Lemon.autoc.fill((255, 255, 255))
        var.Lemon.player.blit(var.Lemon.autoc, (800, 0))
    var.Lemon.number.fill((255, 0, 0))
    var.Lemon.plus1.fill((0, 255, 0))
    var.Lemon.upgrade.fill((0, 0, 255))
    var.Lemon.s = var.Lemon.myfont.render('Amt: ' + str(var.Lemon.num), 0, (0, 0, 0))
    var.Lemon.number.blit(var.Lemon.s, (0, 0))
    var.Lemon.splus1 = var.Lemon.smallfont.render(' cost($' + "{0:.2f}".format(var.Lemon.cost_p) + ')', 0, (0, 0, 0))
    if (var.Lemon.lvl == 5):
        var.Lemon.supgrade = var.Lemon.smallfont.render('Max lvl', 0, (0, 0, 0))
    else:
        var.Lemon.supgrade = var.Lemon.smallfont.render(' cost($' + "{0:.2f}".format(var.Lemon.cost_l) + ')', 0, (0, 0, 0))
    var.Lemon.plus1.blit(var.Lemon.p, (0, 0))
    var.Lemon.upgrade.blit(var.Lemon.u, (0, 0))
    var.Lemon.plus1.blit(var.Lemon.splus1, (30, 10))
    var.Lemon.upgrade.blit(var.Lemon.supgrade, (30, 11))
    var.Lemon.player.blit(img.Lemon, (0, 1))
    var.Lemon.player.blit(var.Lemon.number, (100, 1))
    var.Lemon.player.blit(var.Lemon.plus1, (500, 1))
    var.Lemon.player.blit(var.Lemon.upgrade, (500, 51))
    var.Lemon.player.blit(var.Lemon_download, (150, 61))
    var.Lemon.player.blit(var.Lemon_cur_time, (450, 51))
    var.Lemon.player.set_colorkey((255, 255, 255))

def updateGazeta():
    if (var.Gazeta.autoclick):
        var.Gazeta.autoc.fill((255, 255, 255))
        var.Gazeta.player.blit(var.Gazeta.autoc, (800, 0))
    var.Gazeta.number.fill((255, 0, 0))
    var.Gazeta.plus1.fill((0, 255, 0))
    var.Gazeta.upgrade.fill((0, 0, 255))
    var.Gazeta.s = var.Gazeta.myfont.render('Amt: ' + str(var.Gazeta.num), 0, (0, 0, 0))
    var.Gazeta.number.blit(var.Gazeta.s, (0, 0))
    var.Gazeta.splus1 = var.Gazeta.smallfont.render(' cost($' + "{0:.2f}".format(var.Gazeta.cost_p) + ')', 0, (0, 0, 0))
    if (var.Gazeta.lvl == 5):
        var.Gazeta.supgrade = var.Gazeta.smallfont.render('Max lvl', 0, (0, 0, 0))
    else:
        var.Gazeta.supgrade = var.Gazeta.smallfont.render(' cost($' + "{0:.2f}".format(var.Gazeta.cost_l) + ')', 0, (0, 0, 0))
    var.Gazeta.plus1.blit(var.Gazeta.p, (0, 0))
    var.Gazeta.upgrade.blit(var.Gazeta.u, (0, 0))
    var.Gazeta.plus1.blit(var.Gazeta.splus1, (30, 10))
    var.Gazeta.upgrade.blit(var.Gazeta.supgrade, (30, 11))
    var.Gazeta.player.blit(img.Gazeta, (0, 1))
    var.Gazeta.player.blit(var.Gazeta.number, (100, 1))
    var.Gazeta.player.blit(var.Gazeta.plus1, (500, 1))
    var.Gazeta.player.blit(var.Gazeta.upgrade, (500, 51))
    var.Gazeta.player.blit(var.Gazeta_download, (150, 61))
    var.Gazeta.player.blit(var.Gazeta_cur_time, (450, 51))
    var.Gazeta.player.set_colorkey((255, 255, 255))

def updateCoffee():
    if (var.Coffee.autoclick):
        var.Coffee.autoc.fill((255, 255, 255))
        var.Coffee.player.blit(var.Coffee.autoc, (800, 0))
    var.Coffee.number.fill((255, 0, 0))
    var.Coffee.plus1.fill((0, 255, 0))
    var.Coffee.upgrade.fill((0, 0, 255))
    var.Coffee.s = var.Coffee.myfont.render('Amt: ' + str(var.Coffee.num), 0, (0, 0, 0))
    var.Coffee.number.blit(var.Coffee.s, (0, 0))
    var.Coffee.splus1 = var.Coffee.smallfont.render(' cost($' + "{0:.2f}".format(var.Coffee.cost_p) + ')', 0, (0, 0, 0))
    if (var.Coffee.lvl == 5):
        var.Coffee.supgrade = var.Coffee.smallfont.render('Max lvl', 0, (0, 0, 0))
    else:
        var.Coffee.supgrade = var.Coffee.smallfont.render(' cost($' + "{0:.2f}".format(var.Coffee.cost_l) + ')', 0, (0, 0, 0))
    var.Coffee.plus1.blit(var.Coffee.p, (0, 0))
    var.Coffee.upgrade.blit(var.Coffee.u, (0, 0))
    var.Coffee.plus1.blit(var.Coffee.splus1, (30, 10))
    var.Coffee.upgrade.blit(var.Coffee.supgrade, (30, 11))
    var.Coffee.player.blit(img.Coffee, (0, 1))
    var.Coffee.player.blit(var.Coffee.number, (100, 1))
    var.Coffee.player.blit(var.Coffee.plus1, (500, 1))
    var.Coffee.player.blit(var.Coffee.upgrade, (500, 51))
    var.Coffee.player.blit(var.Coffee_download, (150, 61))
    var.Coffee.player.blit(var.Coffee_cur_time, (450, 51))
    var.Coffee.player.set_colorkey((255, 255, 255))

def updatePizza():
    if (var.Pizza.autoclick):
        var.Pizza.autoc.fill((255, 255, 255))
        var.Pizza.player.blit(var.Pizza.autoc, (800, 0))
    var.Pizza.number.fill((255, 0, 0))
    var.Pizza.plus1.fill((0, 255, 0))
    var.Pizza.upgrade.fill((0, 0, 255))
    var.Pizza.s = var.Pizza.myfont.render('Amt: ' + str(var.Pizza.num), 0, (0, 0, 0))
    var.Pizza.number.blit(var.Pizza.s, (0, 0))
    var.Pizza.splus1 = var.Pizza.smallfont.render(' cost($' + "{0:.2f}".format(var.Pizza.cost_p) + ')', 0, (0, 0, 0))
    if (var.Pizza.lvl == 5):
        var.Pizza.supgrade = var.Pizza.smallfont.render('Max lvl', 0, (0, 0, 0))
    else:
        var.Pizza.supgrade = var.Pizza.smallfont.render(' cost($' + "{0:.2f}".format(var.Pizza.cost_l) + ')', 0, (0, 0, 0))
    var.Pizza.plus1.blit(var.Pizza.p, (0, 0))
    var.Pizza.upgrade.blit(var.Pizza.u, (0, 0))
    var.Pizza.plus1.blit(var.Pizza.splus1, (30, 10))
    var.Pizza.upgrade.blit(var.Pizza.supgrade, (30, 11))
    var.Pizza.player.blit(img.Pizza, (0, 1))
    var.Pizza.player.blit(var.Pizza.number, (100, 1))
    var.Pizza.player.blit(var.Pizza.plus1, (500, 1))
    var.Pizza.player.blit(var.Pizza.upgrade, (500, 51))
    var.Pizza.player.blit(var.Pizza_download, (150, 61))
    var.Pizza.player.blit(var.Pizza_cur_time, (450, 51))
    var.Pizza.player.set_colorkey((255, 255, 255))

def updateRestaurant():
    if (var.Restaurant.autoclick):
        var.Restaurant.autoc.fill((255, 255, 255))
        var.Restaurant.player.blit(var.Restaurant.autoc, (800, 0))
    var.Restaurant.number.fill((255, 0, 0))
    var.Restaurant.plus1.fill((0, 255, 0))
    var.Restaurant.upgrade.fill((0, 0, 255))
    var.Restaurant.s = var.Restaurant.myfont.render('Amt: ' + str(var.Restaurant.num), 0, (0, 0, 0))
    var.Restaurant.number.blit(var.Restaurant.s, (0, 0))
    var.Restaurant.splus1 = var.Restaurant.smallfont.render(' cost($' + "{0:.2f}".format(var.Restaurant.cost_p) + ')', 0, (0, 0, 0))
    if (var.Restaurant.lvl < 5):
        var.Restaurant.supgrade = var.Restaurant.smallfont.render(' cost($' + "{0:.2f}".format(var.Restaurant.cost_l) + ')', 0, (0, 0, 0))
    else:
        var.Restaurant.supgrade = var.Restaurant.smallfont.render('Max lvl', 0, (0, 0, 0))
    var.Restaurant.plus1.blit(var.Restaurant.p, (0, 0))
    var.Restaurant.upgrade.blit(var.Restaurant.u, (0, 0))
    var.Restaurant.plus1.blit(var.Restaurant.splus1, (30, 10))
    var.Restaurant.upgrade.blit(var.Restaurant.supgrade, (30, 11))
    var.Restaurant.player.blit(img.Restaurant, (0, 1))
    var.Restaurant.player.blit(var.Restaurant.number, (100, 1))
    var.Restaurant.player.blit(var.Restaurant.plus1, (500, 1))
    var.Restaurant.player.blit(var.Restaurant.upgrade, (500, 51))
    var.Restaurant.player.blit(var.Restaurant_download, (150, 61))
    var.Restaurant.player.blit(var.Restaurant_cur_time, (450, 51))
    var.Restaurant.player.set_colorkey((255, 255, 255))


def LemonWork():
    if (not var.Lemon_work and var.Lemon.num > 0):
        var.Lemon_work = True
        var.Lemon_time = time.time()

def GazetaWork():
    if (not var.Gazeta_work and var.Gazeta.num > 0):
        var.Gazeta_work = True
        var.Gazeta_time = time.time()

def CoffeeWork():
    if (not var.Coffee_work and var.Coffee.num > 0):
        var.Coffee_work = True
        var.Coffee_time = time.time()

def PizzaWork():
    if (not var.Pizza_work and var.Pizza.num > 0):
        var.Pizza_work = True
        var.Pizza_time = time.time()

def RestaurantWork():
    if (not var.Restaurant_work and var.Restaurant.num > 0):
        var.Restaurant_work = True
        var.Restaurant_time = time.time()

def startWorking(coord):
    if  (coord[0] <= 150 and coord[0] >= 100):
        if (coord[1] <= 202 and coord[1] >= 152):
            LemonWork()
        elif (coord[1] <= 312 and coord[1] >= 262):
            GazetaWork()
        elif (coord[1] <= 422 and coord[1] >= 372):
            CoffeeWork()
        elif (coord[1] <= 532 and coord[1] >= 482):
            PizzaWork()
        elif (coord[1] <= 642 and coord[1] >= 592):
            RestaurantWork()

def getLemonMoney():
    if (var.Lemon_work):
        if (var.Lemon_time + var.Lemon.time() <= time.time()):
            if (not var.Lemon.autoclick):
                var.Lemon_work = False
            else:
                var.Lemon_time = time.time()
            var.Lemon_download.fill((0, 0, 0))
            var.Lemon_cur_time.fill((255, 255, 255))
            t = var.Lemon.smallfont.render('0', 0, (0, 0, 0))
            var.Lemon_cur_time.blit(t, (0, 0))
            var.count_player_money += (var.Lemon.money * var.Lemon.num)
        else:
            temp = 300 * (time.time() - var.Lemon_time) / var.Lemon.time()
            var.Lemon_cur_load = pygame.Surface((temp, 30))
            var.Lemon_cur_load.fill((0, 255, 0))
            var.Lemon_download.blit(var.Lemon_cur_load, (0, 0))
            temp = var.Lemon.time() - (time.time() - var.Lemon_time)
            t = var.Lemon.smallfont.render("{0:.2f}".format(temp), 0, (0, 0, 0))
            var.Lemon_cur_time.fill((255, 255, 255))
            var.Lemon_cur_time.blit(t, (0, 0))

def getGazetaMoney():
    if (var.Gazeta_work):
        if (var.Gazeta_time + var.Gazeta.time() <= time.time()):
            if (not var.Gazeta.autoclick):
                var.Gazeta_work = False
            else:
                var.Gazeta_time = time.time()
            var.Gazeta_download.fill((0, 0, 0))
            var.Gazeta_cur_time.fill((255, 255, 255))
            t = var.Gazeta.smallfont.render('0', 0, (0, 0, 0))
            var.Gazeta_cur_time.blit(t, (0, 0))
            var.count_player_money += (var.Gazeta.money * var.Gazeta.num)
        else:
            temp = 300 * (time.time() - var.Gazeta_time) / var.Gazeta.time()
            var.Gazeta_cur_load = pygame.Surface((temp, 30))
            var.Gazeta_cur_load.fill((0, 255, 0))
            var.Gazeta_download.blit(var.Gazeta_cur_load, (0, 0))
            temp = var.Gazeta.time() - (time.time() - var.Gazeta_time)
            t = var.Gazeta.smallfont.render("{0:.2f}".format(temp), 0, (0, 0, 0))
            var.Gazeta_cur_time.fill((255, 255, 255))
            var.Gazeta_cur_time.blit(t, (0, 0))

def getCoffeeMoney():
    if (var.Coffee_work):
        if (var.Coffee_time + var.Coffee.time() <= time.time()):
            if (not var.Coffee.autoclick):
                var.Coffee_work = False
            else:
                var.Coffee_time = time.time()
            var.Coffee_download.fill((0, 0, 0))
            var.Coffee_cur_time.fill((255, 255, 255))
            t = var.Coffee.smallfont.render('0', 0, (0, 0, 0))
            var.Coffee_cur_time.blit(t, (0, 0))
            var.count_player_money += (var.Coffee.money * var.Coffee.num)
        else:
            temp = 300 * (time.time() - var.Coffee_time) / var.Coffee.time()
            var.Coffee_cur_load = pygame.Surface((temp, 30))
            var.Coffee_cur_load.fill((0, 255, 0))
            var.Coffee_download.blit(var.Coffee_cur_load, (0, 0))
            temp = var.Coffee.time() - (time.time() - var.Coffee_time)
            t = var.Coffee.smallfont.render("{0:.2f}".format(temp), 0, (0, 0, 0))
            var.Coffee_cur_time.fill((255, 255, 255))
            var.Coffee_cur_time.blit(t, (0, 0))

def getPizzaMoney():
    if (var.Pizza_work):
        if (var.Pizza_time + var.Pizza.time() <= time.time()):
            if (not var.Pizza.autoclick):
                var.Pizza_work = False
            else:
                var.Pizza_time = time.time()
            var.Pizza_download.fill((0, 0, 0))
            var.Pizza_cur_time.fill((255, 255, 255))
            t = var.Pizza.smallfont.render('0', 0, (0, 0, 0))
            var.Pizza_cur_time.blit(t, (0, 0))
            var.count_player_money += (var.Pizza.money * var.Pizza.num)
        else:
            temp = 300 * (time.time() - var.Pizza_time) / var.Pizza.time()
            var.Pizza_cur_load = pygame.Surface((temp, 30))
            var.Pizza_cur_load.fill((0, 255, 0))
            var.Pizza_download.blit(var.Pizza_cur_load, (0, 0))
            temp = var.Pizza.time() - (time.time() - var.Pizza_time)
            t = var.Pizza.smallfont.render("{0:.2f}".format(temp), 0, (0, 0, 0))
            var.Pizza_cur_time.fill((255, 255, 255))
            var.Pizza_cur_time.blit(t, (0, 0))

def getRestaurantMoney():
    if (var.Restaurant_work):
        if (var.Restaurant_time + var.Restaurant.time() <= time.time()):
            if (not var.Restaurant.autoclick):
                var.Restaurant_work = False
            else:
                var.Restaurant_time = time.time()
            var.Restaurant_download.fill((0, 0, 0))
            var.Restaurant_cur_time.fill((255, 255, 255))
            t = var.Restaurant.smallfont.render('0', 0, (0, 0, 0))
            var.Restaurant_cur_time.blit(t, (0, 0))
            var.count_player_money += (var.Restaurant.money * var.Restaurant.num)
        else:
            temp = 300 * (time.time() - var.Restaurant_time) / var.Restaurant.time()
            var.Restaurant_cur_load = pygame.Surface((temp, 30))
            var.Restaurant_cur_load.fill((0, 255, 0))
            var.Restaurant_download.blit(var.Restaurant_cur_load, (0, 0))
            temp = var.Restaurant.time() - (time.time() - var.Restaurant_time)
            t = var.Restaurant.smallfont.render("{0:.2f}".format(temp), 0, (0, 0, 0))
            var.Restaurant_cur_time.fill((255, 255, 255))
            var.Restaurant_cur_time.blit(t, (0, 0))

def getMoney():
    getLemonMoney()
    getGazetaMoney()
    getCoffeeMoney()
    getPizzaMoney()
    getRestaurantMoney()

def runAutoclick(coord):
    if (coord[0] <= 900 and coord[0] >= 800):
        if (coord[1] <= 202 and coord[1] >= 101):
            if (var.count_player_money >= var.Lemon.cost_auto and not var.Lemon.autoclick):
                var.Lemon_work = True
                var.Lemon.autoclick = True
                var.count_player_money -= var.Lemon.cost_auto

        if (coord[1] <= 312 and coord[1] >= 211):
            if (var.count_player_money >= var.Gazeta.cost_auto and not var.Gazeta.autoclick):
                var.Gazeta_work = True
                var.Gazeta.autoclick = True
                var.count_player_money -= var.Gazeta.cost_auto

        if (coord[1] <= 422 and coord[1] >= 321):
            if (var.count_player_money >= var.Coffee.cost_auto and not var.Coffee.autoclick):
                var.Coffee_work = True
                var.Coffee.autoclick = True
                var.count_player_money -= var.Coffee.cost_auto

        if (coord[1] <= 532 and coord[1] >= 431):
            if (var.count_player_money >= var.Pizza.cost_auto and not var.Pizza.autoclick):
                var.Pizza_work = True
                var.Pizza.autoclick = True
                var.count_player_money -= var.Pizza.cost_auto

        if (coord[1] <= 642 and coord[1] >= 541):
            if (var.count_player_money >= var.Restaurant.cost_auto and not var.Restaurant.autoclick):
                var.Restaurant_work = True
                var.Restaurant.autoclick = True
                var.count_player_money -= var.Restaurant.cost_auto

def updateScreen():
    var.screen.fill((255, 255, 255))
    var.screen.blit(img.BackGround, (0, 0))
    var.screen.blit(var.GameName, (250, 0))
    var.screen.blit(var.Menu, (930, 100))
    var.screen.blit(var.Lemon.player, (0, 100))
    var.screen.blit(var.Gazeta.player, (0, 210))
    var.screen.blit(var.Coffee.player, (0, 320))
    var.screen.blit(var.Pizza.player, (0, 430))
    var.screen.blit(var.Restaurant.player, (0, 540))
    var.window.blit(var.screen, (0, 0))
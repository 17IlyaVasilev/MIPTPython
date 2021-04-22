import unit
import pygame
import img

pygame.init()

done = True

count_player_money = 0

myfont = pygame.font.SysFont('monospace', 50)
smallfont = pygame.font.SysFont('serif', 30)
font = pygame.font.SysFont('serif', 40)
mouse_coord = ((0, 0))

Lemon = unit.Lemon()
Gazeta = unit.Gazeta()
Coffee = unit.Coffee()
Pizza = unit.Pizza()
Restaurant = unit.Restaurant()

Lemon_work = False
Gazeta_work = False
Coffee_work = False
Pizza_work = False
Restaurant_work = False

Lemon_time = 0
Gazeta_time = 0
Coffee_time = 0
Pizza_time = 0
Restaurant_time = 0

Lemon_cur_time = pygame.Surface((50, 50))
Gazeta_cur_time = pygame.Surface((50, 50))
Coffee_cur_time = pygame.Surface((50, 50))
Pizza_cur_time = pygame.Surface((50, 50))
Restaurant_cur_time = pygame.Surface((50, 50))

Lemon_cur_time.fill((255, 255, 255))
Gazeta_cur_time.fill((255, 255, 255))
Coffee_cur_time.fill((255, 255, 255))
Pizza_cur_time.fill((255, 255, 255))
Restaurant_cur_time.fill((255, 255, 255))

t = Lemon.smallfont.render('0', 0, (0, 0, 0))
t = Gazeta.smallfont.render('0', 0, (0, 0, 0))
t = Coffee.smallfont.render('0', 0, (0, 0, 0))
t = Pizza.smallfont.render('0', 0, (0, 0, 0))
t = Restaurant.smallfont.render('0', 0, (0, 0, 0))

Lemon_cur_time.blit(t, (0, 0))
Gazeta_cur_time.blit(t, (0, 0))
Coffee_cur_time.blit(t, (0, 0))
Pizza_cur_time.blit(t, (0, 0))
Restaurant_cur_time.blit(t, (0, 0))

Lemon_download = pygame.Surface((300, 30))
Gazeta_download = pygame.Surface((300, 30))
Coffee_download = pygame.Surface((300, 30))
Pizza_download = pygame.Surface((300, 30))
Restaurant_download = pygame.Surface((300, 30))

Lemon_cur_load = pygame.Surface((0, 30))
Gazeta_cur_load = pygame.Surface((0, 30))
Coffee_cur_load = pygame.Surface((0, 30))
Pizza_cur_load = pygame.Surface((0, 30))
Restaurant_cur_load = pygame.Surface((0, 30))

namefont = pygame.font.SysFont('serif', 60)
GameName = pygame.Surface((800, 70))
GameName.fill((255, 255, 255))
GN = namefont.render('AdVenture Capitalist by IL1on', 0, (0, 0, 0))
GameName.blit(GN, (0, 0))
GameName.set_colorkey((255, 255, 255))

Menu = pygame.Surface((350, 540))
Menu.blit(img.Menu, (0, 0))

Money = pygame.Surface((350, 50))
Money.fill((0, 255, 0))
money = myfont.render('$' + "{0:.2f}".format(count_player_money), 0, (0, 0, 0))
Money.blit(money, (0, 0))
Menu.blit(Money, (0, 0))

n1 = 'Naruto'
n2 = 'Sasuke'
n3 = 'Kakashi'
n4 = 'Sakura'
n5 = 'Hinata'
n6 = 'Shikomaru'
n7 = 'Neji'
n8 = 'Djeray'
n9 = 'Orochimaru'
n10 = 'You'

m1 = 1000000000
m2 = 50000000
m3 = 2500000
m4 = 100000
m5 = 50000
m6 = 25000
m7 = 10000
m8 = 5000
m9 = 1000
m10 = 0

s1 = smallfont.render('', 0, (0, 0, 0))
s2 = smallfont.render('', 0, (0, 0, 0))
s3 = smallfont.render('', 0, (0, 0, 0))
s4 = smallfont.render('', 0, (0, 0, 0))
s5 = smallfont.render('', 0, (0, 0, 0))
s6 = smallfont.render('', 0, (0, 0, 0))
s7 = smallfont.render('', 0, (0, 0, 0))
s8 = smallfont.render('', 0, (0, 0, 0))
s9 = smallfont.render('', 0, (0, 0, 0))
s10 = smallfont.render('', 0, (255, 255, 255))

place = 10

flag = True

Records = pygame.Surface((175, 50))
Settings = pygame.Surface((175, 50))

Records.blit(img.Menu2, (0, 0))
Settings.blit(img.Menu1, (0, 0))

srecords = font.render('Records', 0, (0, 0, 0))
ssettings = font.render('Settings', 0, (0, 0, 0))

Records.blit(srecords, (0, 0))
Settings.blit(ssettings, (0, 0))

Music = font.render('Music', 0, (0, 0, 0))

Music_load1 = pygame.Surface((200, 10))
Music_load2 = pygame.Surface((200, 10))
Music_load3 = pygame.Surface((200, 10))

Music_load1.fill((0, 0, 0))
Music_load2.fill((0, 0, 0))
Music_load3.fill((0, 0, 0))

Music_play1 = pygame.Surface((250, 50))
Music_play2 = pygame.Surface((250, 50))
Music_play3 = pygame.Surface((250, 50))

Music_real_load1 = pygame.Surface((0, 10))
Music_real_load2 = pygame.Surface((0, 10))
Music_real_load3 = pygame.Surface((0, 10))

Music_play1.fill((255, 255, 255))
Music_play2.fill((255, 255, 255))
Music_play3.fill((255, 255, 255))

Music_play1.blit(img.Play, (0, 0))
Music_play2.blit(img.Play, (0, 0))
Music_play3.blit(img.Play, (0, 0))
Music_play1.blit(Music_load1, (50, 40))
Music_play2.blit(Music_load2, (50, 40))
Music_play3.blit(Music_load3, (50, 40))

Music1 = False
Music2 = False
Music3 = False

Sound = pygame.Surface((50, 50))
Sound.blit(img.SoundOn, (0, 0))
sound = True

window = pygame.display.set_mode((1280, 640))
screen = pygame.Surface((1280, 640))

screen.fill((255, 255, 255))
screen.blit(img.BackGround, (0, 0))
screen.blit(GameName, (250, 0))
screen.blit(Menu, (930, 100))
screen.blit(Lemon.player, (0, 100))
screen.blit(Gazeta.player, (0, 210))
screen.blit(Coffee.player, (0, 320))
screen.blit(Pizza.player, (0, 430))
screen.blit(Restaurant.player, (0, 540))
window.blit(screen, (0, 0))

















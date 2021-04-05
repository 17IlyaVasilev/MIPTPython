import pygame
import var
import img
import unit
import func
import time


pygame.init()

while (var.done):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            var.done = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            var.done = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            var.count_player_money += 1
        if e.type == pygame.MOUSEBUTTONDOWN:
            var.mouse_coord = pygame.mouse.get_pos()
            func.mouse(var.mouse_coord)
            func.startWorking(var.mouse_coord)
            func.runAutoclick(var.mouse_coord)
            func.flagChange(var.mouse_coord)
            func.changeMusic(var.mouse_coord)
            func.soundChange(var.mouse_coord)

    func.getMoney()
    func.updateMenu()
    func.updateLemon()
    func.updateGazeta()
    func.updateCoffee()
    func.updatePizza()
    func.updateRestaurant()
    func.updateScreen()
    pygame.display.update()

pygame.quit()
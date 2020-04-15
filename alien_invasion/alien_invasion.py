
import sys 
import pygame 
from pygame.sprite import Group 

from settings import Settings #class named "Settings" is imported 
from ship import Ship
import game_functions as gf 

def run_game():
    #initialize pygame, settings, and screen object. 
    pygame.init()
    ai_settings= Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alian Invasion")
    
    #make a ship
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in 
    bullets = Group()
    
    #start the main loop for the game 
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        #Get rid of bullets that have disappeared 
        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
        print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)#ai_setting, from the "Setting"
run_game()

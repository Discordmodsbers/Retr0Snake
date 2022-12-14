import pygame
from pygame.locals import *
import os
import sys
import webbrowser
# Game Initialization
pygame.init()
 
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "Retro.ttf"
 
 
# Game Framerate
clock = pygame.time.Clock()
FPS=30
# Main Menu


def main_menu():
 
    menu=True
    selected="start"
    
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    selected="start"
                    pygame.mixer.music.load('sfx/click.wav')
                    pygame.mixer.music.play(1)
                elif event.key==pygame.K_s:
                    selected="quit"
                    pygame.mixer.music.load('sfx/click.wav')
                    pygame.mixer.music.play(1)
                if event.key==pygame.K_SPACE:
                    if selected=="start":
                        pygame.mixer.music.load('sfx/load.wav')
                        pygame.mixer.music.play(1)
                        os.system('python3 snake.py')
                    if selected=="quit":
                        pygame.quit()
                        quit()
                if event.key == pygame.K_PERIOD:
                    print("You have found the hidden key!")
 
        # Main Menu UI
        screen.fill(blue)
        title=text_format("Retr0Snake", font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 75, green)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("PUSSY", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Retr0Snake")

#Initialize the Game
main_menu()

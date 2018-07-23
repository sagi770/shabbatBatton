import pygame
pygame.mixer.init()
pygame.mixer.music.load("mpthreetest.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
    
#playsound.playsound('/var/www/flaskAPP/mpthreetest.mp3', True)

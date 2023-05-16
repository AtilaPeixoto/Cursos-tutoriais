import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load(r"c:\users\meu\music\nova pasta\cbj.mp3")
pygame.mixer.music.play()
pygame.event.wait()
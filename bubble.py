import pygame
import time

pygame.mixer.init()
drum_sound = pygame.mixer.Sound("drum.wav")
list = ['f', 'i','l','i','p']

n = len(list)
for j in range(n-1):
    for i in range(n-j-1):
        if(list[i] > list[i+1]):
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
        drum_sound.play()
        print(list)
        time.sleep(2)
    



import pygame
import time

pygame.mixer.init()
drum_sound = pygame.mixer.Sound("drum.wav")
list = ['f', 'i','l','i','p']

n = len(list)
for i in range(1,n):
    k = list[i]
    j = i - 1
    while(j >= 0 and list[j] > k):
        list[j+1] = list[j]
        j = j - 1

    list[j+1] = k
    drum_sound.play()
    print(list)
    time.sleep(2)

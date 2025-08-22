import pygame
import time

pygame.mixer.init()
drum_sound = pygame.mixer.Sound("drum.wav")

list = ['f','i','l','i','p']
h = [2,1]

n = len(list)

for i in range(len(h)):
    inc = h[i]
    for j in range(inc, n):
        y = list[j]
        k = j - inc
        while(k >= 0 and y <list[k]):
            list[k+inc] = list[k]
            k = k-inc
        list[k+inc] = y

    drum_sound.play()
    print(list)
    time.sleep(2)

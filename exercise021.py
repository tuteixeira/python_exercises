#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('desafio021music')
pygame.mixer.music.play()
input()
pygame.event.wait()

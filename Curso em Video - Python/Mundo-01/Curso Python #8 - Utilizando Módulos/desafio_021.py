'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
from pygame import mixer

mixer.init()
mixer.music.load('desafio_021.mp3')
mixer.music.play()

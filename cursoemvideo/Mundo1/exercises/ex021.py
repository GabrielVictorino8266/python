# Tocando um arquivo mp3.

# Import the modules

import pygame
from pygame import mixer

# Instancia mixer
mixer.init()

# Carrega um arquivo de música
mixer.music.load('ex021.mp3')

# Dá um play na música
mixer.music.play()
print("Tocando a música...")

while True:
    print("-----------------------------------------------")
    print("Pressione P para Pausar.")
    print("Pressione R para dar Play.")
    print("Pressione E para sair.")

    userInput = input(" ")

    if userInput == 'p':

        mixer.music.pause()
        print('Música pausada.')
    elif userInput == 'r':
        mixer.music.unpause()
        print("Música está tocando.")
    elif userInput == 'e':
        print("Você saiu do player")
        break

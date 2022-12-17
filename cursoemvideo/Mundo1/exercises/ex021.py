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
    print("Press 'p' to pause the music")
    print("Press 'r' to resume the music")
    print("Press 'e' to exit the program")

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

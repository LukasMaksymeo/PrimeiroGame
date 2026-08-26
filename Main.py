import Crit
import pygame
import Classes
pygame.init()
import os
os.system('clear') or None
pygame.mixer.music.load('Rememberthat.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print("           Olá Jogador!!!           \n"
      "         Escolha sua classe         \n")
# chama a função "escolha_de_classe" do bloco de Classes e atribui seus respectivos valores


teste = Classes.Paladino()

print(teste)
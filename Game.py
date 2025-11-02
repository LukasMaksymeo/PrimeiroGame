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
      "         Escolha sua classe         \n"
      "", Classes.classe, "")
# chama a função "escolha_de_classe" do bloco de Classes e atribui seus respectivos valores
vida, ataque, Crit_chance, Atq_Crit = Classes.escolha_de_classe(input())

print("hora da batalha ")
inimigo = "goblin"
vida_Inimigo = 30
atq_Inimigo = 4
while(vida > 0 and vida_Inimigo > 0): ### fase de batalha, transformar em uma função ###
    print(inimigo, "atacou você")
    vida = vida - atq_Inimigo
    print("você ataca")
    Atq_Crit = Crit.Critico(Crit_chance, ataque)
    vida_Inimigo = vida_Inimigo - (ataque + Atq_Crit)
    if (vida <= 0):
        print("você morreu!")
    elif (vida_Inimigo <= 0):
        print("você ganhou")
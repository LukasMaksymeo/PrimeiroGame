import Crit
import pygame
pygame.init()
import os          
os.system('clear') or None
pygame.mixer.music.load('PrimeiroGame/Rememberthat.mp3')
pygame.mixer.music.play()
pygame.event.wait()
classe=("Barbaro","Paladino","Assasino")
print("           Olá Jogador!!!           \n"
      "         Escolha sua classe         \n"
      "", classe, "")
opcao = (input())
if (opcao == "barbaro"):
    print("teste barbaro funcionou")
    vida = 30
    ataque = 5
    Crit_chance = [1]
    Atq_Crit = 0
elif (opcao == "paladino"):
    print("teste paladino funcionou")
    vida = 50
    ataque = 3
    Crit_chance = [1]
    Atq_Crit = 0    
elif (opcao == "assasino"):
    print("teste assasino funcionou")
    vida = 20
    ataque = 6
    Crit_chance = [1,2,3]
    Atq_Crit = 0
else:
    print("erro")    
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
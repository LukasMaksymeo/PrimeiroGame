# def teste_vida(palavra_chave):
#     a_valor = 20
#     a_dano = 7
#     b_valor = 30
#     b_dano = 5
#     c_valor = 50
#     c_dano = 2
#     if palavra_chave == "a":
#         return a_valor, a_dano
#     elif palavra_chave == "b":
#         return b_valor, b_dano
#     elif palavra_chave == "c":
#         return c_valor, c_dano
#     else:
#         print("erro")
#
# print("escolha entre a, b ou c")
# vida, dano = teste_vida(input())
#
# print("sua vida tem valor igual a: ",vida, "\nseu dano tem valor de: ", dano)
#
#---------------------------------------------------------------------------------------
#
# import Crit   ###import de um conteudo dentro de outro arquivo na mesma pasta
# vida = 20                   #      vez do jogador
# ataque = 2                  #
# Crit_chance = [1,2]       #
# Atq_Crit = 0
#
#
#
# ###---------------------------------------------------------------------------
# inimigo = "goblin"          #       vez do pc
# vida_Inimigo = 10           #            #
#
#
#
# ###---------------------------------------------------------------------------
# while(vida > 0 and vida_Inimigo > 0): ### fase de batalha, transformar em uma função ###
#     print(inimigo, "atacou você")
#     print("você ataca")
#     Atq_Crit = Crit.Critico(Crit_chance, ataque)
#     vida_Inimigo = vida_Inimigo - (ataque + Atq_Crit)
#     print(Atq_Crit, ataque)
#
#
#
# ###----------------------------------------------------------------------------
# import os           ### comando para limpar o terminal, caso precise
# os.system('clear') or None
# ###----------------------------------------------------------------------------
# ### Comando para fazer lowercase e o cancelar os espaçamentos
# ###----------------------------------------------------------------------------
# from tkinter import* ### Doc que Traz as telas
# janela = Tk()               ### não está funcionando
# janela.mainloop()
#
#
#
###----------------------------------------------------------------------------
# def teste_vida(palavra_chave):
#     a_valor = 20
#     b_valor = 30
#     c_valor = 50
#     if palavra_chave == "a":
#         return a_valor
#     elif palavra_chave == "b":
#         return b_valor
#     elif palavra_chave == "c":
#         return c_valor
#     else:
#         print("erro")
#
# print("escolha entre a, b ou c")
# vida = teste_vida(input())
#
# print("sua vida tem valor igual a: ",vida)
#
###------------------------------------------------------------------------------------
#
# import Classes
# import Crit
# print("hora da batalha ")
# inimigo = "goblin"
# vida_Inimigo = 30
# atq_Inimigo = 4
# while(vida > 0 and vida_Inimigo > 0): ### fase de batalha, transformar em uma função ###
#     print(inimigo, "atacou você")
#     vida = vida - atq_Inimigo
#     print("você ataca")
#     Atq_Crit = Crit.Critico(Crit_chance, ataque)
#     vida_Inimigo = vida_Inimigo - (ataque + Atq_Crit)
#     if (vida <= 0):
#         print("você morreu!")
#     elif (vida_Inimigo <= 0):
#         print("você ganhou")

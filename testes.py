import Crit
vida = 20                   #      vez do jogador
ataque = 2                  #
Crit_chance = [1,2]       #
Atq_Crit = 0            
###---------------------------------------------------------------------------
inimigo = "goblin"          #       vez do pc
vida_Inimigo = 10           #            #
###---------------------------------------------------------------------------
while(vida > 0 and vida_Inimigo > 0): ### fase de batalha, transformar em uma função ###
    print(inimigo, "atacou você")
    print("você ataca")
    Atq_Crit = Crit.Critico(Crit_chance, ataque)
    vida_Inimigo = vida_Inimigo - (ataque + Atq_Crit)
    print(Atq_Crit, ataque)

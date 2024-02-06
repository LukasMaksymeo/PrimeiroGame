import random
Crit_chance = [1,2]
ataque = 2
Atq_Crit = 0
def Critico(Crit_chance, ataque,Atq_Crit):
    Tentativa = [1,2,3,4,5,6,7,8,9,0]
    chances = random.choice(Tentativa)
    if(chances in Crit_chance):
        Atq_Crit = ataque * 2
    else:
        quit
        Atq_Crit = 0
    return Atq_Crit
print(Atq_Crit)

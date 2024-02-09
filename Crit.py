import random
def Critico(Crit_chance, ataque):
    Tentativa = [1,2,3,4,5,6,7,8,9,0]
    chances = random.choice(Tentativa)
    if(chances in Crit_chance):
        Atq_Crit = ataque
    else:
        quit
        Atq_Crit = 0
    return Atq_Crit


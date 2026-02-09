import Classes
import Crit
def testarPersonagem(Player1, Player2, turnos):
    a,v1,v2 = 0
    a1,b1,c1 = Classes.escolhaDeClasse(Player1)
    a2,b2,c2 = Classes.escolhaDeClasse(Player2)
    while a != turnos:
        print("aqui vai a fase de batalha")
        a += 1


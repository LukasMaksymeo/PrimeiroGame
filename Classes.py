from pygame.examples.midi import NullKey

# classe=("Barbaro","Paladino","Assasino")
#
# def escolhaDeClasse(opcao):
#     if (opcao == "barbaro"):
#         print("teste barbaro funcionou")
#         vida = 35
#         ataque = 7
#         Crit_chance = [0]
#         Atq_Crit = 0
#         return vida, ataque, Crit_chance, Atq_Crit ## VER UMA MELHOR FORMA DE LOCALIZAR O ATQ_CRIT
#     elif (opcao == "paladino"):
#         print("teste paladino funcionou")
#         vida = 50
#         ataque = 3
#         Crit_chance = [1]
#         Atq_Crit = 0
#         return vida, ataque, Crit_chance, Atq_Crit
#     elif (opcao == "assasino"):
#         print("teste assasino funcionou")
#         vida = 20
#         ataque = 6
#         Crit_chance = [1,2,3]
#         Atq_Crit = 0
#         return vida, ataque, Crit_chance, Atq_Crit

class Personagem:
    def __init__(self, vida=0, ataque=0,critico=0,bloqueio=0):
        self.vida = vida
        self.ataque = ataque
        self.critico = critico
        self.bloqueio =bloqueio

    def sofrer_dano(self, dano):
        self.vida -= dano
        print(self.vida)
    def realizar_ataque(self):
        return self.ataque

class Barbaro(Personagem):
    def __init__(self):
        super().__init__(vida=35, ataque=7)

class Assassino(Personagem):
    def __init__(self):
        super().__init__(vida=48, ataque=3, critico=5)

class Paladino(Personagem):
    def __init__(self):
        super().__init__(vida=27, ataque=3,critico=2,bloqueio=3)


print("Insira seu dano")
lukas = Assassino()
lukas.sofrer_dano(int(input()))

from pygame.examples.midi import NullKey

class Personagem:
    def __init__(self, vida=0, ataque=0,critico=0,bloqueio=0):
        self.vida = vida
        self.ataque = ataque
        self.critico = critico
        self.bloqueio = bloqueio

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


# print("Insira seu dano")
# lukas = Assassino()
# lukas.sofrer_dano(int(input()))

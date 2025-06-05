from jogadores.jogador import Jogador

class Cavaleiro(Jogador): # Herança
    def __init__(self, nome:str, dano:int, resistencia = 85, armadura="Diamante"):
        self.armadura = armadura
        self.resistencia = resistencia
        super().__init__(nome, dano)

    @property # Decorador retorna apenas como propriedade
    def saude(self):
        return self.__saude

    @saude.setter # Decorador retorna apenas como propriedade
    def saude(self, valor):
        self.saude += max(0, valor)

    def atacar(self):
        print("Atacar polimorfico")        
        print(f"{self.nome} atacou!")
    
    def defender(self):
        print("Defender polimorfico")
        print(f"{self.nome} defendeu!")
    
if __name__ == '__main__':
    cavaleiro = Cavaleiro("Rei Arthur", 80)
    cavaleiro.atacar()

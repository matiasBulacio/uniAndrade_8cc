
class Player:
    host = "localhost: 8080" #global
    #inicializador do objeto
    # passando valores posicionais
    def __init__(self, nome, arma):
        self.nome = nome # autoriza modificação/objeto
        self.arma = arma
    # Getter e Setter (fake)
    #Método que intercepta a visualização
    def get_nome(self):
        print(f"Nome: ${self.nome}")
    # Setter (fake)
    def set_nome(it, nome):
        it.nome = nome

# Aquiles: Player = Player('Aquiles', 'faca')
# print(Aquiles.host, Aquiles.arma)

kratos: Player = Player('Kratos', 'blades of chaos')
print(kratos.set_nome("vivaldi"))
print(kratos.get_nome())
# print(kratos.nome, kratos.arma)

# dante: Player = Player('Dante','oblivion')
# print(dante.nome, dante.arma)




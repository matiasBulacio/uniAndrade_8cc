
class Player:
    host = "localhost: 8080" #global
    #inicializador do objeto
    # passando valores posicionais
    def __init__(self, nome, arma):
        self.nome = nome # autoriza modificação/objeto
        self.arma = arma

class Player2:
    def __init__(self, nome, arma):
        self.nome = nome # autoriza modificação/objeto
        self.arma = arma

kratos: Player = Player('Kratos', 'blades of chaos')
print(kratos.nome, kratos.arma)

dante: Player2 = Player2('Dante','oblivion')
print(dante.nome, dante.arma)


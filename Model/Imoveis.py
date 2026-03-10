from config import conectar

class Imovel:

    def __init__(self, endereco, cidade, valor, quartos, banheiros, id=None):

        self.id = id
        self.endereco = endereco
        self.cidade = cidade
        self.valor = valor
        self.quartos = quartos
        self.banheiros = banheiros

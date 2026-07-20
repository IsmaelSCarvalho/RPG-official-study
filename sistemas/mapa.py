from personagens.inimigos.goblin import Goblin
from personagens.inimigos.esqueleto import Esqueleto
from personagens.inimigos.dragao import Dragao


class Regiao:
    def __init__(self, nome, nivel_recomendado, monstros_possiveis, itens_especificos):
        self.nome = nome
        self.nivel_recomendado = nivel_recomendado
        self.monstros_possiveis = monstros_possiveis # Lista de classes de monstros
        self.itens_especificos = itens_especificos   # Item que dropa nessa região para missões

MAPA_MUNDO = {
    "1": Regiao("Floresta dos Sussurros", 1, [Goblin], "Orelha de Goblin"),
    "2": Regiao("Cripta Esquecida", 4, [Esqueleto], "Ossos Antigos"),
    "3": Regiao("Caverna do Dragão", 7, [Dragao], "Escama de Dragão"),
}


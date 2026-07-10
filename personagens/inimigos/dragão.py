from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha

class Dagrao(Personagem):
    def __init__(self):

        atributos_dagrao = AtributosFicha(
            forca=30,
            defesa=90,
            hp_max=300
        )
        super().__init__(
            nome="Goblin",
            classe="Monstro",
            atributo=atributos_dagrao
        )

from personagens.inimigos.inimigo import Inimigo
from personagens.atributosficha import AtributosFicha

class Dragao(Inimigo):
    def __init__(self, identificador: str = ""):

        atributos_dragao = AtributosFicha(
            forca=30,
            defesa=90,
            hp_max=300,
            sabedoria=13,
            velocidade=25
        )

        nome_completo = f"Dragão {identificador}".strip()


        super().__init__(
            nome=nome_completo,
            atributo=atributos_dragao,
            exp_recompensa=60
        )

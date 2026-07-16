from personagens.inimigos.inimigo import Inimigo
from personagens.atributosficha import AtributosFicha


class Goblin(Inimigo):
    def __init__(self, identificador: str = ""):
        # Criamos a ficha de atributos do Goblin
        atributos_goblin = AtributosFicha(
            forca=2,
            defesa=3,
            hp_max=10,
            sabedoria=0,
            velocidade=1
        )

        # Montamos o nome dele (Ex: "Goblin A" ou apenas "Goblin")
        nome_completo = f"Goblin {identificador}".strip()

        # Chamamos o construtor de Inimigo, passando os dados e a XP que ele dá (ex: 15 de XP)
        super().__init__(
            nome=nome_completo,
            atributo=atributos_goblin,
            exp_recompensa=15
        )

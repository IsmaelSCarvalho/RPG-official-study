from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from personagens.atributo import Atributo

class Arqueiro(Personagem):
    def __init__(self, nome: str):

        atributos_arqueiro = AtributosFicha(forca=7, defesa=12, hp_max=100, sabedoria=2, velocidade=13)

        super().__init__(nome=nome, classe="Flecha das Sobras", atributo=atributos_arqueiro)

        self.atributo_desarmado = "velocidade"
        self.dano_desarmado = "1d5"

        self.visao = Atributo("visao", 25)

    def flechas_de_longo_alcance(self, alvo):
        custo_visao = 5

        if self.visao.total < custo_visao:
            print(f"❌ {self.nome} Arqueiro não tem o auvo a vista! (Restante: {self.visao.total})")
            return 0

        self.visao.base -= custo_visao

        modificador_velocidade = self.atributos.velocidade.total
        dano_fisico = 13 + modificador_velocidade

        print(f"\n🏹 {self.nome} levanta o seu arco em direção do monstro, suas [flechas de longo alcance] são lançadas para o auto e rasgao o ceu em alta velocidade!")
        print(f"✨ Gastou {custo_visao} de Furia! Furia restante: {self.visao.base}")

        dano_sofrido = alvo.receber_dano(dano_fisico)

        print(f"💥 Suas flechas acertam {alvo.nome} causando {dano_sofrido} de dano fisico instantâneo!")

        return dano_sofrido


    def mostrar(self):

        # Chamamos o mostrar da classe mãe para exibir Nome, Força, Defesa e vida
        super().mostrar()

        # Adicionamos o print exclusivo da mana do Mago
        print(f"Velocidade: {self.velocidade.total} ")
        print("=" * 20)
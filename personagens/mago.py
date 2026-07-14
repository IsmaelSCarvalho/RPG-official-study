from personagens.personagem import Personagem
from personagens.atributosficha import AtributosFicha
from personagens.atributo import Atributo


class Mago(Personagem):
    def __init__(self, nome: str):
        # Criamos o pacote de atributos básicos do Mago
        atributos_mago = AtributosFicha(forca=5, defesa=10, hp_max=100, sabedoria=15, velocidade=0)

        # Passamos para a classe mãe
        super().__init__(nome=nome, classe="Mago de Gelo", atributo=atributos_mago)

        self.atributo_desarmado = "sabedoria"
        self.dano_desarmado = "1d6"

        # Adicionamos a mana exclusiva do Mago
        self.mana = Atributo("Mana", 80)

    def lancar_seta_de_gelo(self, alvo):
        custo_mana = 15

        if self.mana.total < custo_mana:
            print(f"❌ {self.nome} Mana insuficiente! (Restante: {self.mana.total})")
            return 0 # Retorna 0 indicando que a magia falhou

        # 2. Gasta a mana (subtraindo direto do valor .base da sua classe Atributo)
        self.mana.base -= custo_mana

        # 3. Calcula o dano: Sabedoria do Mago + Rolagem de 2d6
        # Como não temos a classe Dados importada aqui, podemos simular ou usar uma função simples.
        # Para manter o código limpo, vamos usar o modificador de Sabedoria + um dano fixo/bônus por enquanto:
        modificador_sabedoria = self.atributos.sabedoria.total
        dano_magico = 12 + modificador_sabedoria # Exemplo: 12 de dano base da magia + Sabedoria

        print(f"\n🔮 {self.nome} estende as mãos e dispara uma [Seta de Gelo] azul brilhante!")
        print(f"✨ Gastou {custo_mana} de Mana! Mana restante: {self.mana.base}")

        # 4. Aplica o dano direto no alvo usando o método que criamos!
        dano_sofrido = alvo.receber_dano(dano_magico)

        print(f"💥 O gelo estilhaça em {alvo.nome} causando {dano_sofrido} de dano mágico instantâneo!")

        return dano_sofrido


    def mostrar(self):

        # Chamamos o mostrar da classe mãe para exibir Nome, Força, Defesa e vida
        super().mostrar()

        # Adicionamos o print exclusivo da mana do Mago
        print(f"Mana: {self.mana.total} ")
        print("=" * 20)
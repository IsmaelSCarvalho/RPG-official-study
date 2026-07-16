from sistemas.testes import Testes
from sistemas.dados import Dados
from sistemas.resultados.resultado_ataque import ResultadoAtaque


class Combate:

    @staticmethod
    def fazer_teste(atacante, alvo):
        arma = atacante.arma

        # AJUSTE DA DEFESA: Buscando o valor real na ficha de atributos + armadura
        defesa_alvo = alvo.atributos.defesa.total
        if hasattr(alvo, 'armadura') and alvo.armadura is not None:
            defesa_alvo += alvo.armadura.defesa_fisica

        return Testes.testar(
            personagem=atacante,
            atributo=arma.atributo,
            dificuldade=defesa_alvo  # Usa a defesa calculada corretamente
        )

    @staticmethod
    def atacar(atacante, alvo):
        # 1. Regra de Desarmado
        if atacante.arma is None:
            atributo_ataque = atacante.atributo_desarmado
            dano_base_texto = atacante.dano_desarmado
            print(f"👊 {atacante.nome} Atacar sem arma")
        else:
            atributo_ataque = atacante.arma.atributo
            dano_base_texto = atacante.arma.dano

        # Checa se o atacante tem vida (substituindo o .vivo se você não tiver criado a propriedade)
        if atacante.atributos.hp.total <= 0:
            raise ValueError(f"{atacante.nome} está morto e não pode atacar.")

        if alvo.atributos.hp.total <= 0:
            raise ValueError(f"{alvo.nome} já foi derrotado.")

        # 2. Executa o teste de acerto
        teste = Testes.testar(atacante, atributo_ataque, alvo.atributos.defesa.total)

        # 3. Se errou, retorna o ResultadoAtaque básico sem o dano
        if not teste.sucesso:
            return ResultadoAtaque(
                atacante,
                alvo,
                teste,
                resultado_dano=None  # Passamos None indicando erro
            )

        # 4. CÁLCULO DO DANO "PURO" + FÚRIA
        rolagem_dano = Dados.rolar(dano_base_texto)

        modificador_atributo = getattr(
            atacante.atributos,
            atributo_ataque
        ).total

        dano_furia = 0
        if hasattr(atacante, "furia") and atacante.furia.base > 0:
            dano_furia = atacante.furia.base
            print(f"🔥 FURIA ATIVA! ({dano_furia} de dano)")

        dano_total = max(0, rolagem_dano.total + modificador_atributo + dano_furia)

        if teste.critico:
            dano_total *= 2

        resultado_dano = alvo.receber_dano(dano_total)

        return ResultadoAtaque(
            atacante,
            alvo,
            teste,
            resultado_dano,
        )
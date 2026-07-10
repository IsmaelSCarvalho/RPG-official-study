from sistemas.dados import Dados
from sistemas.resultados.resultado_teste import ResultadoTeste

class Testes:

    @staticmethod
    def testar(personagem, atributo: str, dificuldade: int) -> ResultadoTeste:
        atributo_obj = getattr(personagem.atributos, atributo)
        modificador = atributo_obj.total

        rolagem_d20 = Dados.rolar("1d20")
        dado_puro = rolagem_d20.total

        resultado_final = dado_puro + modificador

        critico = (dado_puro == 20)
        falha_critica = (dado_puro == 1)

        sucesso = (resultado_final >= dificuldade)

        if critico:
            sucesso = True
        if falha_critica:
            sucesso = False

        return ResultadoTeste(
            rolagem=rolagem_d20,
            modificador=modificador,
            resultado=resultado_final,
            dificuldade=dificuldade,
            sucesso=sucesso,
            critico=critico,
            falha_critica=falha_critica,
        )
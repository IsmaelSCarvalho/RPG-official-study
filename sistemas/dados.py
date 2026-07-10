import random
from sistemas.resultados.resultado_rolagem import ResultadoRolagem

class Dados:

    @staticmethod
    def rolar(expressao: str) -> ResultadoRolagem:
        # 1. Trata o texto e separa a quantidade de dados pelas faces
        expressao_limpa = expressao.lower().strip()
        quantidade, faces = expressao_limpa.split("d")

        quantidade = int(quantidade)
        faces = int(faces)

        rolagens_individuais = []

        for _ in range(quantidade):
            numero_sorteado = random.randint(1, faces)
            rolagens_individuais.append(numero_sorteado)

        return ResultadoRolagem(expressao_limpa, rolagens_individuais)
class ResultadoRolagem:
    def __init__(self, expressao: str, rolagem: list ):
        self.expressao = expressao # Guarda o texto digitado (Ex: "2d6")
        self.rolagem = rolagem  # Guarda a lista com cada dado (Ex: [4, 2])
        self.total = sum(rolagem)  # Soma automaticamente todos os números da lista (Ex: 6)4

    def mostrar(self):


        """Exibe no terminal um painel visual bonito da rolagem."""
        print("=" * 40)
        print("          ROLAGEM DE DADOS")
        print("=" * 40)
        print(f"Dados lançados   : {self.expressao}")
        print(f"Dados sorteados  : {self.rolagem}")
        print(f"Soma total       : {self.total}")
        print("=" * 40)



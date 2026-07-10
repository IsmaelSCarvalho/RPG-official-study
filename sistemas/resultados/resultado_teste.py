class ResultadoTeste:
    def __init__(
            self,
            rolagem,
            modificador: int,
            resultado: int,
            dificuldade: int,
            sucesso: bool,
            critico: bool,
            falha_critica: bool
    ):
        self.rolagem = rolagem
        self.modificador = modificador
        self.resultado = resultado
        self.dificuldade = dificuldade
        self.sucesso = sucesso
        self.critico = critico
        self.falha_critica = falha_critica

    def mostrar(self):
        """Exibe na tela o relatório completo do teste do D20."""
        print("=" * 40)
        print("           RESULTADO DO TESTE")
        print("=" * 40)
        print(f"Dado puro (D20) : {self.rolagem.total}")
        print(f"Modificador     : +{self.modificador}")
        print(f"Resultado Final : {self.resultado}")
        print(f"Dificuldade alvo: {self.dificuldade}")
        print("-" * 40)

        # Mensagens especiais para o jogador
        if self.critico:
            print("🔥 SUCESSO CRÍTICO! (20 Natural!)")
        elif self.falha_critica:
            print("💀 FALHA CRÍTICA! (1 Natural...)")
        elif self.sucesso:
            print("✅ SUCESSO!")
        else:
            print("❌ FALHA!")
        print("=" * 40)
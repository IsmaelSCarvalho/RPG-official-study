class ResultadoAtaque:
    def __init__(self, atacante, alvo, teste, resultado_dano=None):
        self.atacante = atacante
        self.alvo = alvo
        self.teste = teste
        self.resultado_dano = resultado_dano

    def mostrar(self):
        """Exibe no terminal a narração visual e matemática do ataque."""
        print("\n" + "⚔️ " * 20)
        print(f"        AÇÃO: {self.atacante.nome} VS {self.alvo.nome}")
        print("⚔️ " * 20)

        # 1. Narração do Acerto/Erro baseada no d20
        # Buscamos a arma ou mostramos "Punhos" dinamicamente
        arma_nome = self.atacante.arma.nome if self.atacante.arma else "os punhos nus"
        print(f"» {self.atacante.nome} avança contra {self.alvo.nome} usando {arma_nome}!")

        print(f"» Modificador de Ataque: +{self.teste.modificador}")
        print(
            f"» Dado Puro (D20): [{self.teste.rolagem.total}] | Total: {self.teste.resultado} vs Defesa: {self.teste.dificuldade}")

        print("-" * 40)

        # 2. Exibição do Veredito e Dano Sofrido
        if not self.teste.sucesso:
            if self.teste.falha_critica:
                print(f"💀 FALHA CRÍTICA! {self.atacante.nome} se desequilibrou feio e ERROU o golpe!")
            else:
                print(f"❌ ERROU! {self.alvo.nome} conseguiu se esquivar do ataque!")
        else:
            # Se entrou aqui, o ataque acertou!
            if self.teste.critico:
                print(f"🔥 SUCESSO CRÍTICO! O golpe atingiu um ponto vital!")
            else:
                print(f"✅ ACERTOU! O golpe encontrou uma brecha na defesa!")

                # Mostra o dano calculado e o HP restante do inimigo
                print(f"💥 Dano Causado: {self.resultado_dano} de dano físico!")

                if self.alvo.atributos.hp.total <= 0:
                    print(f"💀 FANTÁSTICO! {self.alvo.nome} foi completamente derrotado em combate!")
                else:
                    print(f"🩸 {self.alvo.nome} agora tem {self.alvo.atributos.hp.total} de HP restante.")

            print("=" * 40 + "\n")


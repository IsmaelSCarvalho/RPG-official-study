from time import sleep

class Missao:
    def __init__(self,
                 di_missao,
                 titulo,
                 descricao,
                 item_necessario,
                 quantidade_necessaria,
                 xp_recompensa,
                 ouro_recompensa
    ):
        self.id = di_missao
        self.titulo = titulo
        self.descricao = descricao
        self.item_necessario = item_necessario
        self.quantidade_necessaria = quantidade_necessaria
        self.xp_recompensa = xp_recompensa
        self.ouro_recompensa = ouro_recompensa
        self.concluida = False

class GuildaMissoes:
    def __init__(self):
        self.missoes_disponiveis = {
            "1": Missao(
                "1",
                    "Peste Verde",
                    "Traga 3 Orelhas de Goblin da floresta",
                    "Orelha de Goblin",
                3, 50, 40
            ),
            "2": Missao(
                "2",
                "Estudo Ósseos",
                "Traga 6 partes de um esqueleto",
                "Ossos Antigos",
                16, 150, 80
            ),
            "3": Missao(
            "3",
                "O Caçador de Lendas",
                "Traga 1 Escama do Lendario Dragão Branco dos olhos Azuis",
                "Escama de Dragão",
                1, 500, 400
            )
        }
        self.missoes_ativas = {}

    def interagir_npc(self, heroi):
        """Menu do NPC de Missões."""
        print("\n🧓 [Mestre da Guilda]: 'Saudações, aventureiro! Precisa de trabalho?'")

        visitando = True
        while visitando:
            print("\n--- QUADRO DE MISSÕES ---")
            print("[ 1 ] Ver Missões Disponíveis")
            print("[ 2 ] Entregar Itens de Missões Ativas")
            print("[ 3 ] Sair da Guilda")

            opcao = input("\nEscolha um Opção ->")
            if opcao == "1":
                self._listar_disponiveis(heroi)
            elif opcao == "2":
                self._verificar_entregas(heroi)
            elif opcao == "3":
                print(f"\n🧓 [Mestre da Guilda]: Foque vivo la fora! ")
                visitando = False
                sleep(1.5)

    def _listar_disponiveis(self, heroi):
        print("\n📜 --- MISSÕES DISPONÍVEIS ---")
        disponiveis = {k: v for k, v in self.missoes_disponiveis.items() if k not in self.missoes_ativas and not v.concluida}

        if not disponiveis:
            print("Não há novas missões no momento! Volte mais tarde.")
            return
        for k, m in disponiveis.items():
            print(f"[{k}] {m.titulo} (Req: {m.quantidade_necessaria}x {m.item_necessario}) | Recompensa: {m.xp_recompensa} XP / {m.ouro_recompensa} PO")
            print(f"    ↳ Description: {m.descricao}")

        escolha = input("\nDigite o número da missão para aceitar (ou ENTER para voltar): ")
        if escolha in disponiveis:
            missao = disponiveis[escolha]
            self.missoes_ativas[escolha] = missao
            print(f"\n✅ Missão '{missao.titulo}' aceita! Adicionada ao seu diário.")
            sleep(1)

    def _verificar_entregas(self, heroi):
        print("\n📋 --- SEU DIÁRIO DE MISSÕES ---")
        if not self.missoes_ativas:
            print("Você não tem nenhuma missão ativa no momento!")
            return

        for k, m in list(self.missoes_ativas.items()):
            # Contamos quantos itens o herói tem no inventário
            # (Assumindo que seu heroi.inventario.itens é uma lista ou dicionário)
            qtd_no_inventario = heroi.inventario.itens.count(m.item_necessario) if isinstance(heroi.inventario.itens, list) else heroi.inventario.contar.item(m.item_necessario)

            print(f"\n📌 [{k}] {m.titulo}")
            print(f"    Progresso: {qtd_no_inventario}/{m.quantidade_necessaria} {m.item_necessario}")

            if qtd_no_inventario >= m.quantidade_necessaria:
                confirmar = input("  [!] Você tem os itens! Entregues agora? (S/N)").lower()
                if confirmar in 's':
                    # Remove os itens do inventário do herói
                    for _ in range(m.quantidade_necessaria):
                        if isinstance(heroi.inventario.itens, list):
                            heroi.inventario.itens.remove(m.item_necessario)

                    # Entrega a recompensa
                    heroi.ouro += m.ouro_recompensa
                    if hasattr(heroi, 'ganhar_xp'):
                        heroi.ganhar_xp(m.xp_recompensa)
                    else:
                        heroi.nivel += 1 # Backup simples se não tiver método de XP

                    m.concluida = True
                    self.missoes_ativas.pop(k)
                    print(f"\n🎉 Missão Concluída! Você ganhou {m.xp_recompensa} XP e {m.ouro_recompensa} PO!")
                    sleep(1.5)

# Instanciamos a guilda globalmente para o main usar
guilda_global = GuildaMissoes()
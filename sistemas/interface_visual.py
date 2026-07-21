import os
import sys
import pygame

pygame.init()
pygame.font.init()


# Dimensões da janela HD
LARGURA, ALTURA = 1280, 720
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cronicas do Reino - RPG")

# Cores do Tema
BRANCA = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO_OURO = (240, 190, 40)
CINZA_ESCURO = (25, 25, 35)

# Fontes
FONTE_TITULO = pygame.font.SysFont("Georgia", 58, bold=True)
FONTE_MENU = pygame.font.SysFont("Arial", 28, bold=True)
FONTE_HISTORIA = pygame.font.SysFont("Verdana", 22)


class EngineGrafica:

    @staticmethod
    def carregar_imagem(caminho, largura, altura):
        if os.path.exists(caminho): # Testa se o arquivo da imagem realmente está salvo na pasta do projeto.
            img = pygame.image.load(caminho) # Lê o arquivo .png ou .jpg do disco rígido e o converte em um objeto gráfico na memória.
            return pygame.transform.scale(img, (largura, altura)) # Estica ou encolhe a imagem para ajustar exatamente aos 1280x720 pixels da nossa janela.
        else: # Tratamento de erro (fallback). Se você esqueceu de colocar a foto dentro de assets/, o programa não vai quebrar!
            superficie = pygame.Surface((largura, altura))
            superficie.fill(CINZA_ESCURO)
            return superficie

    # Função responsável por rodar o loop de eventos e desenhar o menu inicial do jogo.
    @staticmethod
    def desenhar_menu_principal():
        # Carrega a imagem da Cidade Central para servir de fundo.
        fundo_menu = EngineGrafica. carregar_imagem("personagens_imagens/menu/telademenu.png", LARGURA, ALTURA)
        rodando_menu = True #Variável de controle do loop do menu.
        opcao_selecionada = 0 #Guarda o índice do botão atualmente focado (0 = Novo Jogo, 1 = Carregar, 2 = Sair).
        opcao = ["1. NOVO JOGO", "2. CARREGAR JOGO", "3. SAIR DO JOGO"]
        clock = pygame.time.Clock() # Objeto que controla a taxa de quadros por segundo (FPS) do jogo.

        while rodando_menu:
            # 1. Desenha o Fundo
            TELA.blit(fundo_menu, (0, 0))
            overlay = pygame.Surface((LARGURA, ALTURA)), pygame.SRCALPHA
            overlay.fill((0, 0, 0, 160))
            TELA.blit(overlay, (0, 0))
            # Transforma o texto string "CRÔNICAS DO REINO" em uma imagem de texto colorida em amarelo ouro.
            txt_titulo = FONTE_TITULO.render("CRONICAS DO REINO", True, AMARELO_OURO)
            # Calcula a metade da largura do texto para centralizar perfeitamente o título no meio da tela.
            TELA.blit(txt_titulo, (LARGURA // 2 - txt_titulo.get_width() // 2, 100))

            # Desenhando os Botões do Menu
            for index, opcao in enumerate(opcao):
                cor_texto = AMARELO_OURO if index == opcao_selecionada else BRANCA

                # Define o tamanho e as coordenadas (X, Y) onde cada retângulo de botão será desenhado, espaçando-os verticalmente (index * 85).
                largura_btn, altura_btn = 360, 60
                x_btn = LARGURA // 2 - largura_btn // 2
                y_btn = 270 + (index * 85)
                if index == opcao_selecionada:
                    # Desenha a caixa do botão com cantos arredondados
                    pygame.draw.rect(TELA, (50,50,70), (x_btn, y_btn, largura_btn, altura_btn), border_radius=10)
                    pygame.draw.rect(TELA,AMARELO_OURO, (x_btn, y_btn, largura_btn, altura_btn), 3, border_radius=10 )
                else:
                    pygame.draw.rect(TELA, (20,20,30), (x_btn, y_btn, largura_btn, altura_btn), border_radius=10)
                # Renderiza o texto da opção e o desenha exatamente centralizado dentro do seu botão correspondente.
                txt_op = FONTE_MENU.render(opcao, True, cor_texto)
                TELA.blit(txt_op, (LARGURA // 2 - txt_op.get_width() // 2, y_btn + 14))

            # # 5. Eventos de Teclado
            for evento in pygame.event.get(): # Captura todas as ações feitas pelo jogador (cliques do mouse, teclas pressionadas, fechar janela).
                if evento.type == pygame.QUIT: # Se o jogador clicar no "X" vermelho de fechar a janela, encerra o Pygame e fecha o Python.
                    pygame.quit()
                    sys.exit()

                    # Quando uma tecla é pressionada.
                if evento.type == pygame.KEYDOWN:

                    # K_UP / K_DOWN: Seta para CIMA e Seta para BAIXO. A operação % len(opcoes) (módulo) faz com que a seleção navegue em ciclo (se passar do último, volta para o primeiro).
                    if evento.key == pygame.K_UP:
                        opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
                    elif evento.key == pygame.K_DOWN:
                        opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
                    elif evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                        if opcao_selecionada == 0: # Novo jogo
                            return "NOVO JOGO"
                        elif opcao_selecionada == 2: # Sair
                            pygame.quit()
                            sys.exit()

            pygame.display.flip()
            clock.tick(30)
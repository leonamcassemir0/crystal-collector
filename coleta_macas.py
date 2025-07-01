# Importando bibliotecas necessárias
import pygame
import random
import sys

# Inicializando o pygame
pygame.init()

# Constantes do jogo
LARGURA = 600
ALTURA = 400
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
FPS = 60

# Configuração da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletor de Maçãs - Jogo Atualizado")
clock = pygame.time.Clock()

# Carregamento e redimensionamento das imagens
img_cesta = pygame.image.load("assets/cesta.png")
img_cesta = pygame.transform.scale(img_cesta, (60, 50))

img_maca = pygame.image.load("assets/maca.png")
img_maca = pygame.transform.scale(img_maca, (30, 30))


class Jogador:
    """Classe que representa o jogador (cesta coletora)"""
    def __init__(self, x):
        # Posicionamento e dimensões
        self.x = x
        self.y = ALTURA - 60  # Posição fixa no chão
        self.largura = 60
        self.altura = 50
        self.vel = 5
        self.rapido = False  # Estado de velocidade acelerada

    def mover(self, pontos=0):
        """Controla o movimento da cesta com as setas do teclado"""
        teclas = pygame.key.get_pressed()

        # Velocidade aumenta conforme a pontuação quando espaço é pressionado
        if self.rapido:
            # Aumenta 0.3x a cada 20 pontos
            multiplicador_boost = 2 + (pontos // 20) * 0.3
            velocidade = self.vel * multiplicador_boost
        else:
            velocidade = self.vel

        if teclas[pygame.K_LEFT]:
            self.x -= velocidade
        if teclas[pygame.K_RIGHT]:
            self.x += velocidade

        # Mantém a cesta dentro dos limites da tela
        self.x = max(0, min(self.x, LARGURA - self.largura))

    def desenhar(self):
        """Renderiza a cesta na tela"""
        tela.blit(img_cesta, (self.x, self.y))


class Maca:
    """Classe que representa as maçãs que caem"""
    def __init__(self, velocidade):
        # Posição inicial aleatória no topo da tela
        self.x = random.randint(0, LARGURA - 30)
        self.y = -30
        self.velocidade = velocidade

    def mover(self):
        """Move a maçã para baixo"""
        self.y += self.velocidade

    def desenhar(self):
        """Renderiza a maçã na tela"""
        tela.blit(img_maca, (self.x, self.y))

    def fora_da_tela(self):
        """Verifica se a maçã saiu da tela"""
        return self.y > ALTURA

    def colidiu_com(self, jogador):
        """Detecta colisão entre maçã e cesta"""
        return (
            self.x < jogador.x + jogador.largura and
            self.x + 30 > jogador.x and
            self.y < jogador.y + jogador.altura and
            self.y + 30 > jogador.y
        )


def tela_ajuda():
    """Exibe a tela de ajuda com instruções do jogo"""
    while True:
        tela.fill(BRANCO)

        # Título
        fonte_titulo = pygame.font.Font(None, 48)
        titulo = fonte_titulo.render("AJUDA", True, PRETO)
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 50))

        # Instruções
        fonte_texto = pygame.font.Font(None, 24)
        instrucoes = [
            "OBJETIVO: Colete o máximo de maçãs que conseguir!",
            "",
            "CONTROLES:",
            "<-  -> : Mover a cesta para esquerda/direita",
            "ESPAÇO: Acelerar o movimento da cesta (aumenta com pontos)",
            "",
            "REGRAS:",
            "- Você tem 3 vidas",
            "- Perde uma vida quando uma maçã cai no chão",
            "- A cada 40 pontos, mais maçãs aparecem",
            "- As maçãs caem mais rápido conforme você avança",
            "",
            "Pressione ENTER para voltar ao menu"
        ]

        # Renderiza as instruções
        y_offset = 100
        for linha in instrucoes:
            cor = AZUL if linha.startswith(
                ("CONTROLES:", "REGRAS:")) else PRETO
            texto = fonte_texto.render(linha, True, cor)
            tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, y_offset))
            y_offset += 20

        pygame.display.flip()

        # Processa eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return


def tela_inicial():
    """Exibe o menu principal do jogo"""
    while True:
        tela.fill(BRANCO)

        # Título do jogo
        fonte = pygame.font.Font(None, 60)
        titulo = fonte.render("Coletor de Maçãs", True, PRETO)
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 100))

        # Opções do menu
        fonte_btn = pygame.font.Font(None, 36)
        opcoes = [
            ("ENTER - Jogar", 200),
            ("H - Ajuda", 240),
            ("ESC - Sair", 280)
        ]

        for texto, y in opcoes:
            msg = fonte_btn.render(texto, True, PRETO)
            tela.blit(msg, (LARGURA // 2 - msg.get_width() // 2, y))

        pygame.display.flip()

        # Processa eventos do menu
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return
                elif evento.key == pygame.K_h:
                    tela_ajuda()
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def tela_fim(pontos):
    """Exibe a tela de fim de jogo com opções de reiniciar"""
    while True:
        tela.fill(BRANCO)

        # Título e pontuação
        fonte = pygame.font.Font(None, 60)
        msg = fonte.render("Fim de Jogo", True, PRETO)
        tela.blit(msg, (LARGURA // 2 - msg.get_width() // 2, 100))

        fonte_p = pygame.font.Font(None, 36)
        score = fonte_p.render(f"Pontuação: {pontos}", True, PRETO)
        tela.blit(score, (LARGURA // 2 - score.get_width() // 2, 180))

        # Opções
        restart = fonte_p.render("R = Reiniciar | ESC = Sair", True, PRETO)
        tela.blit(restart, (LARGURA // 2 - restart.get_width() // 2, 250))

        pygame.display.flip()

        # Processa eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def main():
    """Função principal que executa o loop do jogo"""
    tela_inicial()

    # Variáveis do jogo
    pontos = 0
    tempo = 0
    vidas = 3
    jogador = Jogador(LARGURA // 2)
    macas = []
    proxima_maca = 0  # Contador para delay entre maçãs

    rodando = True
    while rodando:
        clock.tick(FPS)
        tempo += 1

        # Processa eventos do pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        # Controla movimento do jogador com boost progressivo
        teclas = pygame.key.get_pressed()
        jogador.rapido = teclas[pygame.K_SPACE]
        jogador.mover(pontos)  # Passa pontuação para calcular velocidade

        # Processa movimento das maçãs e colisões
        for maca in macas[:]:
            maca.mover()
            if maca.colidiu_com(jogador):
                pontos += 1
                macas.remove(maca)
            elif maca.fora_da_tela():
                macas.remove(maca)
                vidas -= 1
                if vidas <= 0:
                    if tela_fim(pontos):
                        main()
                    else:
                        rodando = False

        # Sistema de geração de maçãs com delay independente
        # Gera maçãs a cada 3 segundos, mas com delay entre elas
        if tempo % 180 == 0:  # A cada 3 segundos reinicia o ciclo
            proxima_maca = 0  # Reseta o contador de delay

        quantidade_macas = 1 + (pontos // 40)
        velocidade_maca = 2 + (pontos // 10) * 0.5

        # Gera maçãs com delay de 30 frames (0.5 segundos) entre cada uma
        if proxima_maca < quantidade_macas and tempo % 30 == 0:
            macas.append(Maca(velocidade_maca))
            proxima_maca += 1

        # Reseta contador quando completar o ciclo de 3 segundos
        if tempo % 180 == 0:
            proxima_maca = 0

        # Renderiza tela
        tela.fill(BRANCO)
        for maca in macas:
            maca.desenhar()
        jogador.desenhar()

        # Exibe informações do jogo
        fonte = pygame.font.Font(None, 28)
        informacoes = [
            (f"Pontos: {pontos}", 10),
            (f"Tempo: {tempo // 60}s", 40),
            (f"Vidas: {vidas}", 70)
        ]

        for texto, y in informacoes:
            surface = fonte.render(texto, True, PRETO)
            tela.blit(surface, (10, y))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


# Executa o jogo apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    main()

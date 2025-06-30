# JOGO COLETOR DE MAÇÃS

# Importando bibliotecas
import pygame
import random
import sys

# Iniciando o pygame
pygame.init()

# Tamanho da tela
LARGURA = 600
ALTURA = 400

# Cores (formato RGB - Red, Green, Blue)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Velocidade do jogo (frames por segundo)
FPS = 60

# Criação da tela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletor de Maçãs - Jogo Atualizado")
clock = pygame.time.Clock()

# Carregando imagens da cesta e da maçã
img_cesta = pygame.image.load("cesta.png")
img_cesta = pygame.transform.scale(img_cesta, (60, 50))

img_maca = pygame.image.load("maca.png")
img_maca = pygame.transform.scale(img_maca, (30, 30))


class Jogador:
    """Classe do jogador - uma cesta azul (imagem)
    que se move na parte inferior da tela"""

    def __init__(self, x):
        # Posição inicial do jogador
        self.x = x
        self.y = ALTURA - 60  # Fixo no chão
        self.largura = 60
        self.altura = 50
        self.vel = 5
        self.rapido = False  # Indica se está em velocidade acelerada

    def mover(self):
        """Move o jogador para a esquerda ou
        direita com aceleração via tecla espaço"""
        teclas = pygame.key.get_pressed()
        velocidade = self.vel * (2 if self.rapido else 1)
        if teclas[pygame.K_LEFT]:
            self.x -= velocidade
        if teclas[pygame.K_RIGHT]:
            self.x += velocidade
        self.x = max(0, min(self.x, LARGURA - self.largura))

    def desenhar(self):
        """Desenha a cesta na tela"""
        tela.blit(img_cesta, (self.x, self.y))


class Maca:
    """Classe da maçã - item que cai do topo da tela e deve ser coletado"""

    def __init__(self, velocidade):
        self.x = random.randint(0, LARGURA - 30)
        self.y = -30
        self.velocidade = velocidade

    def mover(self):
        """Faz a maçã descer"""
        self.y += self.velocidade

    def desenhar(self):
        """Desenha a imagem da maçã"""
        tela.blit(img_maca, (self.x, self.y))

    def fora_da_tela(self):
        """Verifica se a maçã passou da parte inferior da tela"""
        return self.y > ALTURA

    def colidiu_com(self, jogador):
        """Verifica colisão entre a maçã e a cesta"""
        return (
            self.x < jogador.x + jogador.largura and
            self.x + 30 > jogador.x and
            self.y < jogador.y + jogador.altura and
            self.y + 30 > jogador.y
        )


def tela_inicial():
    """Tela inicial com título e instruções"""
    while True:
        tela.fill(BRANCO)
        fonte = pygame.font.Font(None, 60)
        titulo = fonte.render("Coletor de Maçãs", True, PRETO)
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 100))

        fonte_btn = pygame.font.Font(None, 36)
        msg = fonte_btn.render("Pressione ENTER para Jogar", True, PRETO)
        tela.blit(msg, (LARGURA // 2 - msg.get_width() // 2, 250))

        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return


def tela_fim(pontos):
    """Tela de fim de jogo com pontuação final"""
    while True:
        tela.fill(BRANCO)
        fonte = pygame.font.Font(None, 60)
        msg = fonte.render("Fim de Jogo", True, PRETO)
        tela.blit(msg, (LARGURA // 2 - msg.get_width() // 2, 100))

        fonte_p = pygame.font.Font(None, 36)
        score = fonte_p.render(f"Pontuação: {pontos}", True, PRETO)
        tela.blit(score, (LARGURA // 2 - score.get_width() // 2, 180))

        restart = fonte_p.render("R = Reiniciar | ESC = Sair", True, PRETO)
        tela.blit(restart, (LARGURA // 2 - restart.get_width() // 2, 250))

        pygame.display.flip()
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
    """Função principal que roda o jogo"""
    tela_inicial()
    pontos = 0
    tempo = 0
    vidas = 3
    dificuldade = 1

    jogadores = [Jogador(LARGURA // 2)]
    macas = [Maca(2)]

    rodando = True
    while rodando:
        clock.tick(FPS)
        tempo += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        teclas = pygame.key.get_pressed()
        for jogador in jogadores:
            jogador.rapido = teclas[pygame.K_SPACE]
            jogador.mover()

        for maca in macas[:]:
            maca.mover()
            colidiu = False
            for jogador in jogadores:
                if maca.colidiu_com(jogador):
                    pontos += 1
                    macas.remove(maca)
                    colidiu = True
                    break
            if not colidiu and maca.fora_da_tela():
                macas.remove(maca)
                vidas -= 1
                if vidas <= 0:
                    if tela_fim(pontos):
                        main()
                    else:
                        rodando = False

        # Atualiza frequência de geração de maçãs com base nos pontos
        if pontos >= 100:
            intervalo_geracao = 60  # 1 segundo
        elif pontos >= 60:
            intervalo_geracao = 180  # 3 segundos
        elif pontos >= 40:
            intervalo_geracao = 300  # 5 segundos
        elif pontos >= 20:
            intervalo_geracao = 480  # 8 segundos
        else:
            intervalo_geracao = 600  # 10 segundos

        # Adiciona uma nova maçã em intervalos regulares baseados na pontuação
        if tempo % intervalo_geracao == 0:
            macas.append(Maca(1 + dificuldade * 0.5))

        # Aumenta a dificuldade gradativamente
        if pontos and pontos % 20 == 0 and dificuldade < pontos // 20 + 1:
            dificuldade += 1
            # Adiciona uma nova cesta como bônus se ainda não foi adicionada
            if len(jogadores) < dificuldade:
                jogadores.append(Jogador(random.randint(0, LARGURA - 60)))
        if pontos and pontos % 20 == 0:
            dificuldade += 1
            for _ in range(dificuldade):
                macas.append(Maca(1 + dificuldade))
            if len(jogadores) < dificuldade:
                jogadores.append(Jogador(random.randint(0, LARGURA - 60)))

        # Limpa e desenha a tela
        tela.fill(BRANCO)
        for maca in macas:
            maca.desenhar()
        for jogador in jogadores:
            jogador.desenhar()

        # Informações do jogo: pontos, tempo e vidas
        fonte = pygame.font.Font(None, 28)
        tela.blit(fonte.render(f"Pontos: {pontos}", True, PRETO), (10, 10))
        tela.blit(fonte.render(
            f"Tempo: {tempo // 60}s", True, PRETO), (10, 40))
        tela.blit(fonte.render(f"Vidas: {vidas}", True, PRETO), (10, 70))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


# Só executa o jogo se este arquivo for executado diretamente
if __name__ == "__main__":
    main()

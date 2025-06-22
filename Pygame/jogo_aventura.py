import pygame

# Inicializar Pygame
pygame.init()

# Configurações da tela
largura = 1000
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Nosso Jogo de Aventura")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Personagem
largura_desejada_personagem = 50
altura_desejada_personagem = 70
personagem_direita_original = pygame.image.load("personagem_direita.png").convert_alpha()
personagem_direita = pygame.transform.scale(personagem_direita_original, (largura_desejada_personagem, altura_desejada_personagem))
personagem_esquerda_original = pygame.image.load("personagem_esquerda.png").convert_alpha()
personagem_esquerda = pygame.transform.scale(personagem_esquerda_original, (largura_desejada_personagem, altura_desejada_personagem))
personagem_imagem_atual = personagem_direita
personagem_x = largura // 2 - personagem_direita.get_width() // 2
personagem_y_base = altura - personagem_direita.get_height()
personagem_y = personagem_y_base
personagem_velocidade = 5
esta_pulando = False
descendo = False
altura_pulo = 35
velocidade_pulo = 4
contador_pulo = 0
vida_personagem = 5
vida_maxima = 5  # Define vida máxima
jogo_ativo = True

# INVULNERABILIDADE
invulneravel = False
tempo_invulneravel = 0
duracao_invulneravel = 2500  # milissegundos

# Fundo
fundo_imagem = pygame.image.load("background.png").convert()
fundo_imagem = pygame.transform.scale(fundo_imagem, (largura, altura))

# Corações com imagens
coracao_cheio_original = pygame.image.load("coracao_cheio.png").convert_alpha()
coracao_cheio = pygame.transform.scale(coracao_cheio_original, (25, 25))

coracao_vazio_original = pygame.image.load("coracao_vazio.png").convert_alpha()
coracao_vazio = pygame.transform.scale(coracao_vazio_original, (25, 25))

# Classe Monstro
class Monstro(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem_arquivo, largura_desejada, altura_desejada):
        super().__init__()
        self.imagem_original = pygame.image.load(imagem_arquivo).convert_alpha()
        self.image = pygame.transform.scale(self.imagem_original, (largura_desejada, altura_desejada))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.posicao_x = float(x)
        self.velocidade = 2
        self.vida = 3
        self.direction = 1
        self.range_movimento = 50
        self.posicao_inicial_x = x

    def update(self):
        self.posicao_x += self.velocidade * self.direction
        self.rect.x = int(self.posicao_x)
        if self.posicao_x >= self.posicao_inicial_x + self.range_movimento:
            self.direction = -1
        elif self.posicao_x <= self.posicao_inicial_x - self.range_movimento:
            self.direction = 1

    def draw(self, tela):
        tela.blit(self.image, self.rect)

# Ataque
def verificar_ataque(personagem_rect, direcao, monstros):
    area_ataque = pygame.Rect(0, 0, 0, 0)
    if direcao == "direita":
        area_ataque.x = personagem_rect.right
    elif direcao == "esquerda":
        area_ataque.x = personagem_rect.left - 30
    area_ataque.y = personagem_rect.top
    area_ataque.width = 30
    area_ataque.height = personagem_rect.height

    for monstro in list(monstros):
        if area_ataque.colliderect(monstro.rect):
            monstro.vida -= 1
            if monstro.vida <= 0:
                return monstro
    return None

# Monstros
def criar_monstros():
    m1 = Monstro(100, altura - 55, "monstro.png", 60, 60)
    m2 = Monstro(600, altura - 55, "monstro.png", 60, 60)
    return [m1, m2]

monstros = criar_monstros()

# Fonte
fonte = pygame.font.Font(None, 36)

# Loop principal
clock = pygame.time.Clock()
rodando = True
while rodando:
    tempo_atual = pygame.time.get_ticks()
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if jogo_ativo:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and not esta_pulando:
                    esta_pulando = True
                    descendo = False
                    contador_pulo = altura_pulo
                elif evento.key == pygame.K_SPACE:
                    direcao_ataque = "direita" if personagem_imagem_atual == personagem_direita else "esquerda"
                    personagem_rect = personagem_imagem_atual.get_rect(topleft=(int(personagem_x), int(personagem_y)))
                    monstro_derrotado = verificar_ataque(personagem_rect, direcao_ataque, monstros)
                    if monstro_derrotado:
                        monstros.remove(monstro_derrotado)
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                personagem_x = largura // 2 - personagem_direita.get_width() // 2
                personagem_y = personagem_y_base
                vida_personagem = vida_maxima
                monstros = criar_monstros()
                jogo_ativo = True
                invulneravel = False

    if jogo_ativo:
        for monstro in monstros:
            monstro.update()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            personagem_x -= personagem_velocidade
            personagem_imagem_atual = personagem_esquerda
        if teclas[pygame.K_RIGHT]:
            personagem_x += personagem_velocidade
            personagem_imagem_atual = personagem_direita

        if esta_pulando:
            if not descendo:
                if contador_pulo > 0:
                    personagem_y -= velocidade_pulo
                    contador_pulo -= 1
                else:
                    descendo = True
            else:
                personagem_y += velocidade_pulo
                if personagem_y >= personagem_y_base:
                    esta_pulando = False
                    descendo = False
                    personagem_y = personagem_y_base

        personagem_x = max(0, min(largura - personagem_imagem_atual.get_width(), personagem_x))

    tela.blit(fundo_imagem, (0, 0))

    if jogo_ativo:
        personagem_rect = personagem_imagem_atual.get_rect(topleft=(int(personagem_x), int(personagem_y)))
        tela.blit(personagem_imagem_atual, (personagem_x, personagem_y))

        # Flash branco se invulnerável
        if invulneravel and ((tempo_atual - tempo_invulneravel) // 150) % 2 == 0:
            overlay = pygame.Surface((largura_desejada_personagem, altura_desejada_personagem), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, 20))
            tela.blit(overlay, (personagem_x, personagem_y))

        for monstro in monstros:
            monstro.draw(tela)

        if not invulneravel:
            for monstro in monstros:
                if personagem_rect.colliderect(monstro.rect):
                    vida_personagem -= 1
                    invulneravel = True
                    tempo_invulneravel = tempo_atual
                    break

        if invulneravel and (tempo_atual - tempo_invulneravel > duracao_invulneravel):
            invulneravel = False

        if vida_personagem <= 0:
            jogo_ativo = False

        # Mostrar vidas com corações cheios e vazios
        for i in range(vida_maxima):
            if i < vida_personagem:
                tela.blit(coracao_cheio, (10 + i * 30, 10))
            else:
                tela.blit(coracao_vazio, (10 + i * 30, 10))

    else:
        texto_game_over = fonte.render("GAME OVER", True, (255, 0, 0))
        texto_reiniciar = fonte.render("Aperte R para reiniciar", True, branco)
        tela.blit(texto_game_over, (largura // 2 - 100, altura // 2 - 30))
        tela.blit(texto_reiniciar, (largura // 2 - 150, altura // 2 + 10))

    pygame.display.flip()

pygame.quit()

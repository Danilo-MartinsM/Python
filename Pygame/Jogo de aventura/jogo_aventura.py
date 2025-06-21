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

# Personagem (seu código do personagem aqui)
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
personagem_velocidade = 0.5
esta_pulando = False
descendo = False
altura_pulo = 300
velocidade_pulo = 0.5
contador_pulo = 0
vida_personagem = 5
jogo_ativo = True  # ← adicionado
tempo_ultimo_dano = 0
cooldown_dano = 500

# Fundo (seu código do fundo aqui)
fundo_imagem = pygame.image.load("background.png").convert()
fundo_imagem = pygame.transform.scale(fundo_imagem, (largura, altura))

# Classe Monstro
class Monstro(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem_arquivo, largura_desejada, altura_desejada):
        super().__init__()
        self.imagem_original = pygame.image.load(imagem_arquivo).convert_alpha()
        self.image = pygame.transform.scale(self.imagem_original, (largura_desejada, altura_desejada))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.posicao_x = float(x)  # ← posição real em float
        self.velocidade = 0.2
        self.vida = 3
        self.direction = 1
        self.range_movimento = 50
        self.posicao_inicial_x = x

    def update(self):
        self.posicao_x += self.velocidade * self.direction
        self.rect.x = int(self.posicao_x)

        limite_direito = self.posicao_inicial_x + self.range_movimento
        limite_esquerdo = self.posicao_inicial_x - self.range_movimento

        if self.posicao_x >= limite_direito:
            self.direction = -1
        elif self.posicao_x <= limite_esquerdo:
            self.direction = 1

    def draw(self, tela):
        tela.blit(self.image, self.rect)


def verificar_ataque(personagem_rect, direcao, monstros):
    area_ataque = pygame.Rect(0, 0, 0, 0)
    if direcao == "direita":
        area_ataque.x = personagem_rect.right
        area_ataque.y = personagem_rect.top
        area_ataque.width = 30
        area_ataque.height = personagem_rect.height
    elif direcao == "esquerda":
        area_ataque.x = personagem_rect.left - 30
        area_ataque.y = personagem_rect.top
        area_ataque.width = 30
        area_ataque.height = personagem_rect.height

    monstro_atingido = None
    for monstro in list(monstros):
        if area_ataque.colliderect(monstro.rect):
            print(f"Monstro atingido! Vida antes: {monstro.vida}")
            monstro.vida -= 1
            print(f"Vida depois: {monstro.vida}")
            if monstro.vida <= 0:
                print("Monstro derrotado!")
                monstro_atingido = monstro
                return monstro_atingido
            return None
    return None


# Criando os monstros
def criar_monstros():
    m1 = Monstro(100, altura - 55, "monstro.png", 60, 60)
    m2 = Monstro(600, altura - 55, "monstro.png", 60, 60)
    return [m1, m2]

monstros = criar_monstros()

# Inicializar fonte
pygame.font.init()
fonte = pygame.font.Font(None, 36)

# Loop do jogo
rodando = True
while rodando:
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
                # Reiniciar o jogo
                personagem_x = largura // 2 - personagem_direita.get_width() // 2
                personagem_y = personagem_y_base
                vida_personagem = 5
                monstros = criar_monstros()
                jogo_ativo = True

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
        tela.blit(personagem_imagem_atual, (personagem_x, personagem_y))
        for monstro in monstros:
            monstro.draw(tela)

        personagem_rect = personagem_imagem_atual.get_rect(topleft=(int(personagem_x), int(personagem_y)))
        tempo_atual = pygame.time.get_ticks()

        for monstro in monstros:
            if personagem_rect.colliderect(monstro.rect):
                if tempo_atual - tempo_ultimo_dano > cooldown_dano:
                    print("O personagem tocou em um monstro! Perdendo vida...")
                    vida_personagem -= 1
                    print(f"Vida do personagem: {vida_personagem}")
                    tempo_ultimo_dano = tempo_atual

        if vida_personagem <= 0:
            jogo_ativo = False

        texto_vida = fonte.render(f"Vida: {vida_personagem}", True, (255, 0, 0))
        tela.blit(texto_vida, (10, 10))
    else:
        texto_game_over = fonte.render("GAME OVER", True, (255, 0, 0))
        texto_reiniciar = fonte.render("Aperte R para reiniciar", True, (255, 255, 255))
        tela.blit(texto_game_over, (largura // 2 - 100, altura // 2 - 30))
        tela.blit(texto_reiniciar, (largura // 2 - 150, altura // 2 + 10))

    pygame.display.flip()

# Encerrar Pygame
pygame.quit()

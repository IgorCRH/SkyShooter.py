import pygame
import sys
import random
import time

# Inicialização do pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sky Shooter - Médio")

# Cores
white = (255, 255, 255)  # Adicione esta linha para definir a cor branca
black = (0, 0, 0)
red = (255, 0, 0)

# Carregar imagens
player_image = pygame.image.load("personagem.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (100, 100))
player_rect = player_image.get_rect()
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Classe para o personagem
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed = 5
        self.lives = 5  # Vidas iniciais

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = -self.rect.height
            self.speed = random.randint(3, 8)

# Classe para o projétil (bala)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Inicializando pontuação e o tempo
score = 0
start_time = time.time()
game_duration = 6 * 60
victory = False

# Loop principal do jogo
running = True
clock = pygame.time.Clock()


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_b:  # Disparar ao pressionar a tecla B
                player.shoot()

    # Criação de inimigos em intervalos
    if random.randint(0, 100) < 2:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    all_sprites.update()

    # Verificação de colisões entre inimigos e balas
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for enemy in hits:
        score += 5

    # Verificação de colisões entre jogador e inimigos
    hits_player = pygame.sprite.spritecollide(player, enemies, True)
    if hits_player:
        player.lives -= 1
        if player.lives <= 0:
            running = False

    # Verificação de vitória e derrota
    elapsed_time = time.time() - start_time
    if score >= 200 and elapsed_time < game_duration:
        running = False
        victory = True
    elif elapsed_time >= game_duration:
        running = False
        victory = False

    # Renderização
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    
    # Exibição das vidas e pontuação na tela
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {player.lives}", True, black)
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(lives_text, (10, 10))
    screen.blit(score_text, (10, 40))
    
    # Exibição do cronômetro
    remaining_time = max(0, game_duration - elapsed_time)
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    time_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, black)
    screen.blit(time_text, (10, 70))
    
    pygame.display.flip()

    clock.tick(60)

# Exibir tela de game over
game_over_font = pygame.font.Font(None, 72)
if victory:
    game_over_text = game_over_font.render("VICTORY!", True, black)
else:
    game_over_text = game_over_font.render("GAME OVER", True, black)

game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Esperar alguns segundos antes de encerrar o jogo
pygame.time.wait(3000)

pygame.quit()
sys.exit()

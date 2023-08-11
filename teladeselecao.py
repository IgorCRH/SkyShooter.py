import pygame
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Seleção de Dificuldade - Sky Shooter")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)  # Cor cinza

# Fonte
font = pygame.font.Font(None, 36)

# Texto
title_text = font.render("Seleção de Dificuldade - Sky Shooter", True, black)

# Posição do texto
title_rect = title_text.get_rect(center=(screen_width // 2, 100))

# Dimensões dos botões
button_width = 200
button_height = 50

# Loop principal da tela de seleção de dificuldade
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 200 <= mouse_pos[1] <= 250:  # Área correspondente ao botão "Fácil"
                import jogofacil  # Redirecionar para jogofacil.py
            elif 300 <= mouse_pos[1] <= 350:  # Área correspondente ao botão "Médio"
                import jogomedio  # Redirecionar para jogomedio.py
            elif 400 <= mouse_pos[1] <= 450:  # Área correspondente ao botão "Difícil"
                import jogodificil  # Redirecionar para jogodificil.py

    screen.fill(white)
    
    screen.blit(title_text, title_rect)  # Renderizar o título
    
    # Desenhar retângulos para as áreas de seleção
    pygame.draw.rect(screen, gray, (screen_width // 2 - button_width // 2, 200, button_width, button_height))
    pygame.draw.rect(screen, gray, (screen_width // 2 - button_width // 2, 300, button_width, button_height))
    pygame.draw.rect(screen, gray, (screen_width // 2 - button_width // 2, 400, button_width, button_height))
    
    facil_text = font.render("Fácil", True, black)
    medio_text = font.render("Médio", True, black)
    dificil_text = font.render("Difícil", True, black)
    
    # Renderizar os textos dentro das áreas de seleção
    screen.blit(facil_text, (screen_width // 2 - facil_text.get_width() // 2, 210))
    screen.blit(medio_text, (screen_width // 2 - medio_text.get_width() // 2, 310))
    screen.blit(dificil_text, (screen_width // 2 - dificil_text.get_width() // 2, 410))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

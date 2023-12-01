import pygame
import sys
from game import Game

print(pygame.__version__)

pygame.init()

icono = pygame.image.load('sounds/code_icon-icons.com_61210.png')
pygame.display.set_icon(icono)

title = pygame.font.Font(None, 40)
score = title.render('Score', True, (255, 255, 255))
next_surface = title.render("Next", True, (255, 255, 255))
game_over_surface = title.render('GAME OVER', True, (255, 255, 255))

dark_blue = (44, 44, 127)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rectangule = pygame.Rect(320, 215, 170, 180)

SCREEN = pygame.display.set_mode((500, 620))
pygame.display.set_caption("TetrisDemo by Dario Plaza Leon")


pygame.mixer.music.load('sounds/tetris_theme.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

clock = pygame.time.Clock()

GAME = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if GAME.game_over:
                GAME.game_over = False
                GAME.reset()
            if event.key == pygame.K_LEFT and GAME.game_over == False:
                GAME.move_left()
            if event.key == pygame.K_RIGHT and GAME.game_over == False:
                GAME.move_right()
            if event.key == pygame.K_DOWN and GAME.game_over == False:
                GAME.move_down()
                GAME.update_score(0, 1)
            if event.key == pygame.K_UP and GAME.game_over == False:
                GAME.rotate()
        if event.type == GAME_UPDATE and GAME.game_over == False:
            GAME.move_down()

    score_value = title.render(str(GAME.score), True, (255, 255, 255))

    SCREEN.fill(dark_blue)
    SCREEN.blit(score, (365, 20, 50, 50))
    SCREEN.blit(next_surface, (374, 189, 50, 50))

    if GAME.game_over:
        SCREEN.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(SCREEN, (59, 85, 162), score_rect, 0, 10)
    SCREEN.blit(score_value, score_value.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(SCREEN, (59, 85, 162), next_rectangule, 0, 10)

    GAME.draw(SCREEN)

    pygame.display.update()
    clock.tick(60)

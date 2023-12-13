import pygame
import time
import random

pygame.init()

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
BLUE = (125, 200, 255)

# 창크기
window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

block = 20
# 유닛 사이즈, 속도
snake_block_size = (block)
snake_speed = 10
snake_list = []

def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block_size, snake_block_size])

def game_loop():
    global snake_speed
    game_over = False
    game_exit = False

    # 초기 위치
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # 초기 생성
    snake_list.append([x1, y1])
    snake_length = 1

    # 초기 음식 생성
    food_x = round(random.randrange(0, window_width - snake_block_size) / block) * block
    food_y = round(random.randrange(0, window_height - snake_block_size) / block) * block

    #게임 오버
    while not game_exit:
        while game_over:
            window.fill(BLACK)
            font_style = pygame.font.SysFont(None, 70)
            font_style1 = pygame.font.SysFont(None, 100)
            formatted_snake_length = f"{snake_length-1:2}"
            message1 = font_style.render("Score : " + str(formatted_snake_length) , True, BLUE)
            message2 = font_style1.render("Game Over!", True, BLUE)
            message3 = font_style.render("R - Retry", True, BLUE)
            message4 = font_style.render("Q - Quit", True, BLUE)

            message1_width = message1.get_width()
            message2_width = message2.get_width()
            message3_width = message3.get_width()
            message4_width = message4.get_width()

            window.blit(message1, [(window_width - message1_width) / 2, window_height / 3 - 80])
            window.blit(message2, [(window_width - message2_width) / 2, window_height / 3 + 40])
            window.blit(message3, [(window_width - message3_width) / 2, window_height / 3 + 210])
            window.blit(message4, [(window_width - message4_width) / 2, window_height / 3 + 280])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game_over = False
                        x1 = window_width / 2
                        y1 = window_height / 2
                        snake_list.clear()
                        snake_list.append([x1, y1])
                        snake_length = 1
                        snake_speed = 13
                        food_x = round(random.randrange(0, window_width - snake_block_size) / block) * block
                        food_y = round(random.randrange(0, window_height - snake_block_size) / block) * block

        #키 입력
        if x1 < food_x:
                x1_change = snake_block_size
        elif x1 > food_x:
                x1_change = -snake_block_size
        else:
                x1_change = 0

        if y1 < food_y:
            y1_change = snake_block_size
        elif y1 > food_y:
            y1_change = -snake_block_size
        else:
            y1_change = 0

            current_direction = 'RIGHT'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != 'RIGHT':
                    current_direction = 'LEFT'
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and current_direction != 'LEFT':
                    current_direction = 'RIGHT'
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and current_direction != 'DOWN':
                    current_direction = 'UP'
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and current_direction != 'UP':
                    current_direction = 'DOWN'
                    y1_change = snake_block_size
                    x1_change = 0

        # 화면 경계
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        pygame.draw.rect(window, YELLOW, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        # 성장
        if len(snake_list) > snake_length:
            del snake_list[0]

        # 할복
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # 유닛
        draw_snake(snake_block_size, snake_list)

        # 음식 섭취시
        if x1 == food_x and y1 == food_y:
            snake_length += 1
            snake_speed += 1
            food_x = round(random.randrange(0, window_width - snake_block_size) / block) * block
            food_y = round(random.randrange(0, window_height - snake_block_size) / block) * block

        # 화면 재설정
        pygame.display.update()

        # 게임 스피드
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

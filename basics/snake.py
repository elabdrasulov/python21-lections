# import pygame,sys,time,random
# from pygame.locals import *
# # Определить цветовые переменные
# redColour = pygame.Color(255,0,0)
# blackColour = pygame.Color(0,0,0)
# whiteColour = pygame.Color(255,255,255)
# greyColour = pygame.Color(150,150,150)

# def gameOver(playSurface,score):
#     gameOverFont = pygame.font.SysFont('arial.ttf',54)
#     gameOverSurf = gameOverFont.render('Game Over!', True, greyColour)
#     gameOverRect = gameOverSurf.get_rect()
#     gameOverRect.midtop = (300, 10)
#     playSurface.blit(gameOverSurf, gameOverRect)
#     scoreFont = pygame.font.SysFont('arial.ttf',54)
#     scoreSurf = scoreFont.render('Score:'+str(score), True, greyColour)
#     scoreRect = scoreSurf.get_rect()
#     scoreRect.midtop = (300, 50)
#     playSurface.blit(scoreSurf, scoreRect)
#     pygame.display.flip()
#     time.sleep(5)
#     pygame.quit()
#     sys.exit()

# def main():
#     # Инициализировать pygame
#     pygame.init()
#     fpsClock = pygame.time.Clock()
#     # Создать слой отображения pygame
#     playSurface = pygame.display.set_mode((600,460))
#     pygame.display.set_caption('Snake Game')
#     # Инициализировать переменные
#     snakePosition = [100,100] #   Положение головы змеи
#     snakeSegments = [[100,100]] #   Тело змеи, изначально единица
#     raspberryPosition = [300,300] # Исходное положение малины
#     raspberrySpawned = 1 # Количество малины - 1
#     direction = 'right' # Первоначальное направление правильное
#     changeDirection = direction
#     score = 0 # Первоначальная оценка
    
#     while True:
#         # Обнаруживать события pygame, такие как нажатия клавиш
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == KEYDOWN:
#                 # Определить события клавиатуры
#                 if event.key == K_RIGHT or event.key == ord('d'):
#                     changeDirection = 'right'
#                 if event.key == K_LEFT or event.key == ord('a'):
#                     changeDirection = 'left'
#                 if event.key == K_UP or event.key == ord('w'):
#                     changeDirection = 'up'
#                 if event.key == K_DOWN or event.key == ord('s'):
#                     changeDirection = 'down'
#                 if event.key == K_ESCAPE:
#                     pygame.event.post(pygame.event.Event(QUIT))
#         # Определить, введено ли обратное направление
#         if changeDirection == 'right' and not direction == 'left':
#             direction = changeDirection
#         if changeDirection == 'left' and not direction == 'right':
#             direction = changeDirection
#         if changeDirection == 'up' and not direction == 'down':
#             direction = changeDirection
#         if changeDirection == 'down' and not direction == 'up':
#             direction = changeDirection
#         # Переместите координаты головы змеи в соответствии с направлением
#         if direction == 'right':
#             snakePosition[0] += 20
#         if direction == 'left':
#             snakePosition[0] -= 20
#         if direction == 'up':
#             snakePosition[1] -= 20
#         if direction == 'down':
#             snakePosition[1] += 20
#         # Увеличиваем длину змейки
#         snakeSegments.insert(0,list(snakePosition))
#         # Определить, съели ли малину
#         if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
#             raspberrySpawned = 0
#         else:
#             snakeSegments.pop()
#         # Если вы едите малину, восстанавливайте малину
#         if raspberrySpawned == 0:
#             x = random.randrange(1,30)
#             y = random.randrange(1,23)
#             raspberryPosition = [int(x*20),int(y*20)]
#             raspberrySpawned = 1
#             score += 1
#         # Рисуем слой отображения pygame
#         playSurface.fill(blackColour)
#         for position in snakeSegments:
#             pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
#             pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1],20,20))
#         # Обновить слой отображения pygame
#         pygame.display.flip()
#         # Определить, мертв ли ​​он
#         if snakePosition[0] > 600 or snakePosition[0] < 0:
#             gameOver(playSurface,score)
#         if snakePosition[1] > 460 or snakePosition[1] < 0:
#             gameOver(playSurface,score)
#         for snakeBody in snakeSegments[1:]:
#             if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
#                 gameOver(playSurface,score)
#         # Контроль скорости игры
#         fpsClock.tick(5)

# if __name__ == "__main__":
#     main()

# importing libraries
import pygame
import time
import random
 
snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake pod kapotom')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
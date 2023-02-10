import pygame as pg
from random import randrange

# create window/screen for game to show up on
WINDOW = 1000
# since game is in form of grid break into tiles
TILE_SIZE = 50
# tuple that defines range for rand coordinates
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
def get_random_position(): return [randrange(*RANGE), randrange(*RANGE)]


snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
# time step is delay between snake moves in msecs
time, time_step = 0, 110
screen = pg.display.set_mode([WINDOW] * 2)
# instance of clock class to set frame rate
clock = pg.time.Clock()

# main loop of program
while True:
    # check for closing of program
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        # handle change direction keys
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)
    screen.fill('black')
    # draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    # move snake in place
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
        pg.display.flip()
    clock.tick(60)

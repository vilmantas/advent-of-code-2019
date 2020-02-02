import pygame, sys, time, random, math
from enum import Enum
from pygame.locals import*



class Direction(Enum):
    UP = 'U',
    RIGHT = 'R',
    DOWN = 'D',
    LEFT = 'L'

class Path(object):

    direction: Direction
    distance: int

    def __init__(self, data: str): 

        dir_token = data[0]

        if dir_token == 'R':
            self.direction = Direction.RIGHT
        elif dir_token == 'L':
            self.direction = Direction.LEFT
        elif dir_token == 'U':
            self.direction = Direction.UP
        elif dir_token == 'D':
            self.direction = Direction.DOWN

        self.distance = int(data[1:])
        pass

    def __str__(self):
        return f'{self.direction}, {self.distance}'

    def __repr__(self):
        return f'{self.direction}, {self.distance}'

def generate_next_text(surface, direction, distance, left_pos): 
    text_next = font.render(f'{direction} {distance}', True, (255, 255, 255), (0, 0, 0))
    text_next_rect = text_next.get_rect()
    text_next_rect.left = left_pos
    
    pygame.draw.rect(surface,(0,0,0),(left_pos,0,left_pos + 200,17))

    surface.blit(text_next, text_next_rect)   

def generate_endpoint(current_point: (int, int), direction: Direction, distance: int):  
    
    end_point = (0, 0)

    if direction is Direction.UP:
        end_point = (starting_point[0], starting_point[1] - distance)
    elif direction is Direction.DOWN:
        end_point = (starting_point[0], starting_point[1] + distance)
    elif direction is Direction.LEFT:
        end_point = (starting_point[0] - distance, starting_point[1])
    elif direction is Direction.RIGHT:
        end_point = (starting_point[0] + distance, starting_point[1])

    return end_point


WINDOW_HEIGHT = 900
WINDOW_WIDTH = 1440

HEIGHT = 101
WIDTH = 101


if __name__ == "__main__":

    pixels = []

    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(0)
        pixels.append(row)

    # pygame.init()
    # window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

    input_file = open('input-3.txt', 'r')
    data = input_file.read().split('\n')

    lines = [[Path(token) for token in line.split(',')] for line in data]  

    starting_point = (math.floor(WIDTH / 2) + 1, math.floor(HEIGHT / 2) + 1)

    print(starting_point)

    paths = [Path('U15')]

    for path in paths:

        x, y = starting_point

        if path.direction == Direction.UP:
            
            end_point = (x + path.distance, y)

        end_x, end_y = end_point

        if path.direction == Direction.UP:
            for i in range(path.distance):
                pixels[x + i][y] = 1

        if path.direction == Direction.DOWN:
            for i in range(x, end_x):
                pixels[i]




        starting_point = end_point

    # font = pygame.font.Font('freesansbold.ttf', 16) 
    
    # text = font.render('Next instruction: ', True, (255, 255, 255), (0, 0, 0)) 
    # text_rect = text.get_rect()

    # left_pos = text_rect.right + 10;

    # window_surface.blit(text, text_rect) 

    # for line in lines: 
    #     color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    #     for i in range(len(line)):

    #         path = line[i]

    #         if i + 1 <= len(line) - 1:
    #             next_path = line[i + 1]
    #             generate_next_text(window_surface, next_path.direction.name, next_path.distance, left_pos)

    #         end_point = generate_endpoint(starting_point, path.direction, path.distance // 25)

    #         pygame.draw.line(window_surface, color, starting_point, end_point, 2)

    #         starting_point = end_point
            
    #         pygame.display.update()

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    # pass
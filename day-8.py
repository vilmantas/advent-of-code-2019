import pygame, time


data = open('input-8.txt').readlines()

WIDTH = 25
HEIGHT = 6

def main_method():

    layers_count = int(len(data[0]) / (WIDTH * HEIGHT))

    layers = []

    for i in range(layers_count):
        rows = []

        for y in range(HEIGHT):
            one = y * WIDTH + (HEIGHT * WIDTH * i)
            two = y * WIDTH + (HEIGHT * WIDTH * i) + WIDTH
            rows.append(data[0][one:two])

        layers.append(rows)

    max_zeroes = 656
    max_zeroes_layer = []

    for layer in layers:
        zeroes = 0
        
        for row in layer:
            for i in range(len(row)):
                if int(row[i]) == 0:
                    zeroes = zeroes + 1


        if zeroes < max_zeroes:
            max_zeroes = zeroes
            max_zeroes_layer = layer

    ones_count = 0
    twos_count = 0

    for row in max_zeroes_layer:
        for j in range(len(row)):
            if int(row[j]) == 1:
                ones_count += 1
            elif int(row[j]) == 2:
                twos_count += 1

    # PART 1
    # print(ones_count * twos_count)

    return layers


def second_method(layers: []): 

    result = []

    for i in range(HEIGHT):
        result.append([])
        for j in range(WIDTH):
            result[i].append(3)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            val = int(layers[0][i][j])
            if val == 1 or val == 0:
                result[i][j] = val

    for i in range(HEIGHT):
        for j in range(WIDTH):
            val = result[i][j]

            if val == 3:

                for layer in layers:
                    layer_val = int(layer[i][j])
                    if layer_val == 1 or layer_val == 0:
                        result[i][j] = layer_val
                        break;

    return result

WINDOW_HEIGHT = 60 + 20
WINDOW_WIDTH = 250 + 20

if __name__ == "__main__":
    layers = main_method()

    layer = second_method(layers)

    pygame.init()
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

    bg = (83, 75, 98)

    for i in range(int(WINDOW_WIDTH / 10)):
        pygame.draw.rect(window_surface, bg, (i * 10, 0, 10, 10))
        time.sleep(0.025)
        pygame.display.update()

    for i in range(int(WINDOW_WIDTH / 10)):
        pygame.draw.rect(window_surface, bg, (i * 10, WINDOW_HEIGHT - 10, 10, 10))
        time.sleep(0.025)
        pygame.display.update()

    for i in range(int(WINDOW_HEIGHT / 10)):
        pygame.draw.rect(window_surface, bg, (0, i * 10 + 10, 10, 10))
        time.sleep(0.025)
        pygame.display.update()

    for i in range(int(WINDOW_HEIGHT / 10)):
        pygame.draw.rect(window_surface, bg, (WINDOW_WIDTH - 10, i * 10 + 10, 10, 10))
        time.sleep(0.025)
        pygame.display.update()        


    for row in range(len(layer)):
        for val in range(len(layer[row])):
            color = (164, 153, 179)
            if layer[row][val] == 1:
                color = (255, 255, 255)
            pygame.draw.rect(window_surface, color, (10 + val * 10, 10 + row * 10, 10, 10))
            time.sleep(0.0125)
            pygame.display.update()




    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()

    pass
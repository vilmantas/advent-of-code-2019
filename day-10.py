from dataclasses import dataclass

@dataclass
class Tile(object):

    name: str
    x: int
    y: int
    isasteroid: bool
    isvalid = True
    visible_asteroids = 0
    blocked_by = ''

    def __repr__(self):
        if not self.isvalid:
            return 'B' + self.blocked_by
        if self.isasteroid:
            return 'ASTER'
        else:
            return 'EMPTY'

    def distance_to_tile(self, totile):
        return (totile.x - self.x, totile.y - self.y)

    def block(self, blocker: str):
        self.isvalid = False
        self.blocked_by = blocker

class Map(object):

    def __init__(self, raw_data: []):

        self.tiles = []
        self.length = len(raw_data[0])
        self.height = len(raw_data)

        count = 0

        for row in range(len(raw_data)):
            for tile in range(len(raw_data[row])):
                tile_value = raw_data[row][tile]
                self.tiles.append(Tile(str(count).zfill(4),tile, row, tile_value != '.'))
                count += 1
                    

        pass

def block_hidden_asteroids(main_tile: Tile, visible_tile: Tile, asteroid_tiles: []):

    distances = visible_tile.distance_to_tile(main_tile)

    tiles = [ x for x in asteroid_tiles.copy() if x.isvalid ]

    tiles.remove(visible_tile)

    if distances[0] == 0:
        for tile in [x for x in tiles if x.x == main_tile.x]:

            blocked_distance = tile.distance_to_tile(main_tile)

            if distances[1] >= 0 and blocked_distance[1] < 0: 
                continue

            tile.block(visible_tile.name)
        
        return

    if distances[1] == 0:
        for tile in [x for x in tiles if x.y == main_tile.y]:

            blocked_distance = tile.distance_to_tile(main_tile)

            if distances[0] >= 0 and blocked_distance[0] < 0: 
                continue

            tile.block(visible_tile.name)

        return



    for j in range(len(tiles)):

        blocked_tile = tiles[j]

        blocked_distances = blocked_tile.distance_to_tile(main_tile)

        if distances[0] > 0 and blocked_distances[0] <= 0:
            continue

        if distances[1] > 0 and blocked_distances[1] <= 0:
            continue

        if blocked_distances[0] % distances[0] == 0 and blocked_distances[1] % distances[1] == 0:
            blocked_tile.block(visible_tile.name)

    pass

def detect_visible_asteroids(tile: Tile, asteroid_map: Map):

    visible_tiles = 0

    tiles = [x for x in asteroid_map.tiles.copy() if x.isasteroid]

    for i in tiles:
        i.isvalid = True

    tiles.remove(tile)

    for i in range(len(tiles)):

        inspected_tile = tiles[i]

        if not inspected_tile.isvalid:
            continue

        visible_tiles += 1

        block_hidden_asteroids(tile, inspected_tile, tiles)

    tile.visible_asteroids = visible_tiles

    pass


data = open('input-10.txt', 'r').read().split('\n')

if __name__ == "__main__":

    asteroid_map = Map(data)

    max = -25565

    for tile in asteroid_map.tiles:
        if tile.isasteroid and tile.x == 5 and tile.y == 8:
            detect_visible_asteroids(tile, asteroid_map)

    for i in asteroid_map.tiles:
        if i.visible_asteroids > max:
            max = i.visible_asteroids

    print(max)
    pass
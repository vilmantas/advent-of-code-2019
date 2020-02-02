
planets_list_list = []


class Planet(object):

    planets_in_orbit: []

    name: str

    def __init__(self, name: str):
        self.name = name
        self.planets_in_orbit = []

    def __repr__(self):
        return f'{self.name} ){[ x.name for x in self.planets_in_orbit]}'

class PlanetList(object):

    def __init__(self, planets: []):
        self.planets = planets

    def __repr__(self):
        return f'{[x.name for x in self.planets]}'

    def __str__(self):
        return f'{[x.name for x in self.planets]}'

    def last_planet(self):
        return self.planets[-1:][0]

def list_planets(planet: Planet, current_planets: PlanetList):

    if current_planets == None:
        current_planets = PlanetList([planet])
    else:
        current_planets.planets.append(planet)
        

    if len(planet.planets_in_orbit) == 0:
        planets_list_list.append(current_planets)
    else:
        for i in planet.planets_in_orbit:
            list_planets(i, PlanetList(current_planets.planets[:]))

def track_main_planet(planets: [], planet: Planet, part_1: bool): 

    count = 0

    planet_list = PlanetList([])

    while True:

        center = [x for x in planets if planet in x.planets_in_orbit]

        if len(center) != 0:
            planet_list.planets.append(planet)
            planet = center[0]
            count += 1
        else:
            if part_1:
                return count
            else: 
                return planet_list

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

if __name__ == "__main__":

    planets = []
    

    planet_names = []

    data = open('input-6.txt', 'r').readlines()

    for item in data:

        name, orbiter = str.rstrip(item).split(')')

        planet_names.append(name)
        planet_names.append(orbiter)

    planet_names = set(planet_names)

    planets = [Planet(x) for x in planet_names]

    for item in data:
        name, orbiter = str.rstrip(item).split(')')

        for planet in planets:
            if planet.name == name:

                orbiter = next(x for x in planets if x.name == orbiter)

                planet.planets_in_orbit.append(orbiter)

    count = 0

    longest_orbits = {}

    [list_planets(x, None) for x in planets]
    
    part_1 = False

    # PART 1
    sum = 0

    # PART 2
    lists = []

    for planet in planets:
        if part_1:
            sum += track_main_planet(planets, planet)

    # PART 2
    graph = {} 

    for planet in planets:
        graph[planet.name] = [x.name for x in planet.planets_in_orbit]

        graph[planet.name] = graph[planet.name] + [x.name for x in planets if planet.name in [p.name for p in x.planets_in_orbit]]

    z = find_path(graph, 'YOU', 'SAN')

    print(len(z) - 3)

    pass
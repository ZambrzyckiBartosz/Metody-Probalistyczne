import math

cities = []
city_names = []


class City:
    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.population = int(data[2])
        self.latitude = float(data[3])
        self.longitude = float(data[4])

    def distance(self, other):
        return math.sqrt((self.longitude - other.longitude) ** 2 + (self.latitude - other.latitude) ** 2)

    def __repr__(self):
        return str(self.id)


def ReadInput():
    with open("spain.txt", 'r') as f:
        f.readline()
        for lines in f:
            lines = lines.split()
            if lines:
                cities.append(City(lines))
                city_names.append(lines[1])


def find_routes(CityList):
    N = len(CityList)
    routes = []

    def backtrack(current, mask):
        if len(current) == N:
            routes.append(list(current))
            return
        for i in range(N):
            if not (mask & (1 << i)):
                current.append(CityList[i])
                backtrack(current, mask | (1 << i))
                current.pop()

    backtrack([], 0)
    return routes


def silnia(n):
    w = 1
    for i in range(1, n + 1):
        w *= i
    return w


def findpath(Routes):
    minpath = float('inf')
    shortestpath = []
    for route in Routes:
        distance = 0.0
        for i in range(len(route) - 1):
            distance += route[i].distance(route[i + 1])
        if len(route) > 0:
            distance += route[-1].distance(route[0])
        if distance < minpath:
            minpath = distance
            shortestpath = route
    return minpath, shortestpath


def expectedcomb(n, m):
    licz = silnia(n + m - 1)
    mian = silnia(m) * silnia(n - 1)
    return licz // mian


def findcomb(CityList, m):
    n = len(CityList)
    comb = []

    def backtrackt(start, current):
        if len(current) == m:
            comb.append(list(current))
            return
        for i in range(start, n):
            current.append(CityList[i])
            backtrackt(i, current)
            current.pop()

    backtrackt(0, [])
    return comb


def bestpop(route, selectedc):
    totalpop = sum(city.population for city in selectedc)
    targetpop = totalpop / 2
    bestdiff = float('inf')
    bestrut = []
    best_sum = 0
    for rut in route:
        unique_cities = []
        for city in rut:
            if city not in unique_cities:
                unique_cities.append(city)
        current = sum(city.population for city in unique_cities)
        if abs(current - targetpop) < bestdiff:
            bestdiff = abs(current - targetpop)
            bestrut = rut
            best_sum = current
    return bestrut, best_sum,targetpop


if __name__ == '__main__':
    ReadInput()

    n = int(input())
    m = int(input())

    selected_cities = cities[:n]

    print(f"Oczekiwana silnia: {silnia(n)}")

    routes = find_routes(selected_cities)
    for i in range(len(routes)):
        print(f"{i + 1}: {routes[i]}")

    min_dist, shortest = findpath(routes)
    print(f"Najkrotsza trasa: {[c.name for c in shortest]}, dlugosc: {min_dist}")

    n = int(input())
    m = int(input())
    print(f"Oczekiwane {expectedcomb(n, m)}")

    comb = findcomb(selected_cities, m)
    for i in range(len(comb)):
        print(f"{i + 1}: {comb[i]}")

    bestsub, subpop,avg= bestpop(comb, selected_cities)
    names = [city.name for city in bestsub]
    print(f"Najlepsza trasa: {names}, populacja najblizsza: {subpop}, polowa populacji: {avg}")
import math
from math import inf
from typing import assert_never

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
        return str(self.name)
def ReadInput():
    with open("italy.txt", 'r') as f:
        f.readline()
        for lines in f:
            lines = lines.split()
            if lines:
                cities.append(City(lines))
                city_names.append(lines[1])


def find_routes(CityList, K):
    N = len(CityList)
    routes = []
    if K > N:
        return []

    def backtrack(current, mask):
        if len(current) == K:
            routes.append(list(current))
            return
        for i in range(N):
            if not (mask & (1 << i)):
                current.append(CityList[i])
                backtrack(current, mask | (1 << i))
                current.pop()

    backtrack([], 0)
    return routes
def findCombinations(CityList, K):
    N = len(CityList)
    if K > N:
        return []
    routes = []
    def backtrack(current, start_position):
        if len(current) == K:
            routes.append(list(current))
            return
        for i in range(start_position, N):
            current.append(CityList[i])
            backtrack(current, i + 1)
            current.pop()
    backtrack([], 0)
    return routes

def findpath(Routes):
    minpath = float('inf')
    shortestpath = []
    for route in Routes:
        distance = 0.0
        for i in range(len(route) - 1):
            distance += route[i].distance(route[i + 1])
        distance += route[-1].distance(route[0])
        if distance < minpath:
            minpath = distance
            shortestpath = route
    return minpath, shortestpath

def countPopulation(Routes,cities):
    overall = 0
    diff = float('inf')
    answer = []
    for city in cities:
        overall += city.population
    overall = overall / 2
    for route in Routes:
        Routepopulation = 0
        for i in range(len(route)):
            Routepopulation += route[i].population
        if abs(Routepopulation - overall) < diff:
            diff = abs(Routepopulation - overall)
            answer = route
    return diff,answer
if __name__ == '__main__':
    ReadInput()
    routes = find_routes(cities[:5], 3)
    for route in routes:
        print(route)
    print(findpath(routes))
    combinations = findCombinations(cities[:5], 3)
    for combination in combinations:
        print(combination)
    print(countPopulation(combinations, cities[:5]))
import time
import random
from functools import lru_cache
from collections import Counter
import math


class generator:
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m
        self.X = []

    def generate_data(self, N):
        X0 = time.time()
        X0 = int(X0 % self.m)
        self.X = []
        self.X.append(X0)
        for _ in range(N - 1):
            X0 = ((self.a * X0) + self.c) % self.m
            self.X.append(X0)

    def partition(self, K):
        KSize = float(self.m / K)
        mapa: dict[float, int] = {}
        for i in range(1, K + 1):
            high = i * KSize
            mapa[high] = 0
        for c in self.X:
            idx = int(c // KSize)
            if idx >= K:
                idx = K - 1
            serialized = (idx + 1) * KSize
            mapa[serialized] += 1
        return mapa


def monte_carlo(n, k, counter: int = 100000):
    success = 0
    for i in range(counter):
        orzel = 0;
        found = False
        for _ in range(n):
            rzut = random.randint(0, 1);
            if rzut == 1:
                orzel += 1
                if orzel == k:
                    found = True
                    break
            else:
                orzel = 0
        if found == True:
            success += 1
    return success / counter


class rejestrowy:
    def __init__(self, seed: int):
        self.state = seed & 0xFFFFFFFF
        if self.state == 0:
            self.state = 1
        self.X: list[float] = []

    def next_float(self) -> float:
        for _ in range(32):
            lsb = self.state & 1
            self.state >>= 1
            if lsb == 1:
                self.state ^= 0x80200003
        return self.state / 0xFFFFFFFF

    def generatedata(self, N: int):
        self.X = []
        for _ in range(N):
            self.X.append(self.next_float())

    def conditional(self, K: int) -> list[list[int]]:
        matrix = [[0 for _ in range(K)] for _ in range(K)]
        for i in range(len(self.X) - 1):
            current = self.X[i]
            next = self.X[i + 1]
            row = int(current * K)
            column = int(next * K)
            if row >= K:
                row = K - 1
            if column >= K:
                column = K - 1
            matrix[row][column] += 1
        return matrix


def pole(R, counter=100000):
    hit = 0
    for _ in range(counter):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        wpisane = (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25
        rog = (x ** 2 + y ** 2) <= R ** 2
        if wpisane and rog:
            hit += 1
    return hit / counter


def lastq(word):
    word = word.lower()
    counters = Counter(word)
    letters = sorted(counters.keys())
    start_value = tuple(counters[l] for l in letters)
    n = len(word)

    @lru_cache(None)
    def pos(left, index):
        if sum(left) == 0:
            return 1
        suma = 0
        for i in range(len(letters)):
            if left[i] > 0 and i != index:
                nowe = list(left)
                nowe[i] -= 1
                suma += pos(tuple(nowe), i)
        return suma

    good = pos(start_value, -1)
    allpos = math.factorial(n)
    for c in start_value:
        allpos //= math.factorial(c)

    return good,allpos,good/allpos

if __name__ == "__main__":
    N = int(input())
    K = int(input())

    gen = generator(a=1664525, c=1013904223, m=2 ** 32)

    gen.generate_data(N)
    result = gen.partition(K)
    for border, count in result.items():
        print(border, count)

    N = int(input())
    K = int(input())
    print(monte_carlo(N, K))
    N = int(input())
    K = int(input())
    gen = rejestrowy(seed=12345)
    gen.generatedata(N)
    result = gen.conditional(K)
    for row in result:
        print(row)

    print(lastq("mississippi"))
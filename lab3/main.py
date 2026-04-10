import time
import random
import math

def gen50to150():
    seed = random.random()
    a = 50
    b = 150
    x = a + seed*(b - a)
    return int(x)

def dyskretny():
    seed = random.random()

    if random < 0.2: return 1
    if random < 0.5: return 2
    if random < 0.9: return 3
    return 4


if __name__ == "__main__":
     n = 10000;
     result = []
     for i in range(n):
        print(gen50to150())    

     res = [gen50to150() for _ in range(n)]
     

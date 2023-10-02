import random
from threading import Lock
from copy import deepcopy
from project.map1 import map_


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):

    def __init__(self, map_=list()):
        self.map_ = map_
        self.x, self.y = 0, 0
        self.floor = 0
        self.cache = []
        self.no_way = 0

    def choose_init(self):
        while True:
            z = self.floor
            #z = random.randint(0, len(self.map_) - 1)
            x = random.randint(0, len(self.map_[z]) - 1)
            y = random.randint(0, len(self.map_[z][x]) - 1)
            if self.map_[z][x][y]['name'] != 'Garden':
                break
        self.x, self.y = x, y
        self.floor = z
        self.cache += [self.map_[z][x][y]]

    def change_floor(self, up, down):
        self.floor += up - down
        self.cache += [map_[self.floor][self.x][self.y]]

    def change_location(self, way, steps):
        x, y = self.x, self.y
        if way == 0:
            y += steps
        elif way == 1:
            x += steps
        elif way == 2:
            y -= steps
        elif way == 3:
            x -= steps

        if not (0 <= x < len(map_[self.floor])) or not (0 <= y < len(map_[self.floor][x])):
            self.no_way = 1
        else:
            self.no_way = 0
            self.cache += [map_[self.floor][x][y]]
            self.x = x
            self.y = y


if __name__ == '__main__':
    a = Game(map_)
    a.choose_init()
    print(a.cache)

    a = Game()
    print(a.change_location(1, 2))
    print(a.cache)

    a = Game()
    print(a.change_location(3, 2))
    print(a.cache)
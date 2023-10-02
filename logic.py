import random
from threading import Lock
from copy import deepcopy
from project.map import map_


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

    def __init__(self, cache=list()):
        self.cache = cache
        self.map_ = map_
        key = list(self.map_.keys())[random.randint(0, len(self.map_) - 1)]
        self.cache += [self.map_[key]]
        x, y = map(int, key.split('-'))
        self.x, self.y = x, y


    def get(self, dir, steps):
        x, y = self.x, self.y
        if dir == 0:
            y += steps
        elif dir == 1:
            x += steps
        elif dir == 2:
            y -= steps
        elif dir == 3:
            x -= steps

        key = '-'.join([str(x), str(y)])
        if key not in self.map_:
            self.cache += ['You can\'t go this way. Try again']
        else:
            self.cache += [self.map_[key]]
            self.x = x
            self.y = y

a = Game()
print(a.cache)

a = Game()
print(a.get(1, 2))
print(a.cache)

a = Game()
print(a.get(3, 2))
print(a.cache)
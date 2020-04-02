class Asteroid:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:

    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {"E": "N"}
        self.direction = turns[self.direction]


class MissAsteroidError(Exception):
    pass
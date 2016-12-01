#!/usr/bin/python
import sys


class area_map:
    def __init__(self):
        self._map = set()

    def get(self, location):
        if tuple(location) in self._map:
            return True
        return False

    def set(self, location):
        self._map.add(tuple(location))


def travel(map, location, orientation, instruction):
    if instruction[0] == 'R':
        orientation += 90
    elif instruction[0] == 'L':
        orientation -= 90

    orientation %= 360

    if orientation == 0:
        index = 0
        factor = 1
    elif orientation == 90:
        index = 1
        factor = 1
    elif orientation == 180:
        index = 0
        factor = -1
    elif orientation == 270:
        index = 1
        factor = -1

    for i in range(int(instruction[1:])):
        location[index] += factor
        if map.get(location):
            print location

        map.set(location)

    return location, orientation


if __name__ == '__main__':
    location = [0, 0]
    orientation = 0
    visiting_map = area_map()

    with open(sys.argv[1], 'r') as f:
        instructions = f.read().strip("\n").split(", ")
        for instruction in instructions:
            location, orientation = travel(visiting_map, location, orientation, instruction)

        print location



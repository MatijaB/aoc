#!/usr/bin/python
import sys

NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'


def move(location, instruction):
    if instruction == NORTH:
        return location[0], location[1]+1
    if instruction == SOUTH:
        return location[0], location[1]-1
    if instruction == EAST:
        return location[0]+1, location[1]
    if instruction == WEST:
        return location[0]-1, location[1]

if __name__ == '__main__':
    location = (0, 0)
    already_visited = set()
    already_visited.add(location)

    gift_count = 1

    with open(sys.argv[1], 'r') as f:
        instructions = f.read().strip("\n")
        for instruction in instructions:
            location = move(location, instruction)
            if location not in already_visited:
                gift_count += 1
                already_visited.add(location)

    print gift_count




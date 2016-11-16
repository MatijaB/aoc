#!/usr/bin/python
import sys

OPEN_BRACKET = '('
CLOSED_BRACKET = ')'

def calculate(brackets):
    floor = 0
    for bracket in brackets:
        if bracket == OPEN_BRACKET:
            floor += 1
        elif bracket == CLOSED_BRACKET:
            floor -= 1

    return floor

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        brackets = f.read().strip("\n")
        print brackets
        print calculate(brackets)
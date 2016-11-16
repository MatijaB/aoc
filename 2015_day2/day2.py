#!/usr/bin/python
import sys


def calculate_for_one(dimensions):
    areas = list()
    for i in range(3):
        areas.append(dimensions[i]*dimensions[(i+1) % 3])

    return sum(2*x for x in areas) + min(areas)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        complete_sum = 0

        dimension_bundles = f.read().strip("\n").split("\n")

        for dimensions in dimension_bundles:
            dimensions = [int(d) for d in dimensions.split("x")]
            complete_sum += calculate_for_one(dimensions)

    print complete_sum

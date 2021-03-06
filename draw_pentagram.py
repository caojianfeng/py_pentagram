#!/usr/bin/env python
from turtle import *
from configs import *
edge_count = 5
angle = 144
angle_out = -72


def draw_pentagram(size):
    for n in range(edge_count):
        forward(size)
        right(angle)

def draw_pentagram_edge(size):
    for n in range(edge_count*2):
        forward(size*(1-GOLDEN_SECTION))
        right(angle_out if n % 2 == 0 else angle)

def main():
    setpos(-100, 0)
    draw_pentagram(200)
    draw_pentagram_edge(200)
    done()


if __name__ == "__main__":
    main()

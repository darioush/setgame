# -*- encoding: utf-8 -*-
from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    purple = 3


class Shape(Enum):
    diamond = 1
    squiggle = 2
    oval = 3


class Shading(Enum):
    solid = 1
    empty = 2
    striped = 3


class Number(Enum):
    one = 1
    two = 2
    three = 3

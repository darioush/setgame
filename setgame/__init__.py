# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from itertools import combinations
from random import shuffle

from setgame.types import Color, Shape, Shading, Number


SET_LENGTH = 3
INITIAL_COUNT = 12
DEAL_COUNT = 3


class NoSetFound(Exception):
    pass


class GameOver(Exception):
    pass


class Card(object):
    def __init__(self, color, shape, shading, number):
        self.color, self.shape, self.shading, self.number = \
            color, shape, shading, number

    def __repr__(self):
        return "{0} {1} {2} {3}".format(*map(
            lambda enum_item: enum_item.name,
            (self.color, self.shape, self.shading, self.number)))

    @staticmethod
    def is_set(cards):
        colors = set(map(lambda card: card.color, cards))
        shapes = set(map(lambda card: card.shape, cards))
        shadings = set(map(lambda card: card.shading, cards))
        numbers = set(map(lambda card: card.number, cards))

        def all_unique(properties):
            return len(properties) == len(cards)

        def all_same(properties):
            return len(properties) == 1
        return all(all_unique(properties) or all_same(properties)
                   for properties in (colors, shapes, shadings, numbers))


class Board(object):
    def __init__(self):
        self.cards = []

    def extend(self, cards):
        return self.cards.extend(cards)

    def remove(self, cards):
        self.cards = [card for card in self.cards if card not in cards]

    def find_set(self):
        for maybe_set in combinations(self.cards, SET_LENGTH):
            if Card.is_set(maybe_set):
                return maybe_set
        raise NoSetFound()


class SetGame(object):
    def __init__(self):
        self.deck = [Card(color, shape, shading, number)
                     for color in Color
                     for shape in Shape
                     for shading in Shading
                     for number in Number]
        shuffle(self.deck)
        self.board = Board()
        self.deal(INITIAL_COUNT)

    def deal(self, count):
        if len(self.deck) == 0:
            raise GameOver()
        self.board.extend(self.deck[:count])
        self.deck = self.deck[count:]

    def play(self):
        sets_found = []
        try:
            while True:
                try:
                    while True:
                        set_found = self.board.find_set()
                        self.board.remove(set_found)
                        sets_found.append(set_found)
                except NoSetFound:
                    self.deal(DEAL_COUNT)
        except GameOver:
            return sets_found

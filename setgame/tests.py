# -*- encoding: utf-8 -*-
from __future__ import absolute_import
import pytest

from setgame import Board, Card, SetGame, NoSetFound, INITIAL_COUNT
from setgame.types import Color, Shape, Shading, Number

EXAMPLE_SET = (
    Card(Color.red, Shape.diamond, Shading.solid, Number.one),
    Card(Color.red, Shape.squiggle, Shading.empty, Number.one),
    Card(Color.red, Shape.oval, Shading.striped, Number.one),
)


EXAMPLE_NOT_SET = (
    Card(Color.red, Shape.diamond, Shading.solid, Number.one),
    Card(Color.green, Shape.squiggle, Shading.empty, Number.one),
    Card(Color.red, Shape.oval, Shading.striped, Number.one),
)


def test_set_isset():
    assert Card.is_set(EXAMPLE_SET)


def test_set_is_not_set():
    assert not Card.is_set(EXAMPLE_NOT_SET)


def test_finds_set():
    board = Board()
    board.extend(EXAMPLE_SET)
    assert EXAMPLE_SET == board.find_set()


def test_finds_set():
    board = Board()
    # Add irrelevant card
    board.extend([Card(Color.red, Shape.diamond, Shading.solid, Number.two)])
    board.extend(EXAMPLE_SET)
    assert EXAMPLE_SET == board.find_set()


def test_no_set_to_find():
    board = Board()
    board.extend(EXAMPLE_NOT_SET)
    with pytest.raises(NoSetFound):
        board.find_set()


def test_initialize_game():
    game = SetGame()
    assert len(game.deck) == 3*3*3*3 - INITIAL_COUNT


def test_initialize_game_nodups():
    game = SetGame()
    assert len(game.deck) == len(set(game.deck))


def test_play():
    game = SetGame()
    sets = game.play()
    assert all(Card.is_set(set) for set in sets)
    assert len(game.deck) == 0
    with pytest.raises(NoSetFound):
        game.board.find_set()

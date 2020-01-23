#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import unittest
import Board
import Ship
import Game


class test_Game(unittest.TestCase):

	def test_find_ship_location(self):
		b_test = Board.Board(7)
		ships_size = (4, 3, 3, 2, 2, 1, 1, 1, 1)
		ships = [Ship.Ship(b_test, x) for x in ships_size]
		for i in range(len(ships_size)):
			ships[i].name = 'B' + str(i + 1)
		game = Game.Game(b_test, ships)
		game.play()

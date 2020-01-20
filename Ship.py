#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import random
import Board

class Ship:
	def __init__(self, size=4):
		self.size = size
		self.position = list()

	def choose_starting_square(self):
		x, y = random.randrange(8), random.randrange(8)
		return x, y

	def disposition(self, board):
		ship_placed = False
		while not ship_placed:
			self.position = list()
			cpt = 0
			x, y = self.choose_starting_square()
			while not board.array_occupied[x][y] and cpt + y < board.size and cpt < self.size:
				self.position.append((x, y + cpt))
				cpt = cpt + 1
			if cpt == self.size:
				ship_placed = True
				for x in self.position:
					board.array_occupied[x[0]][x[1]] = True


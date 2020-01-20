#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import random
import Board

class Ship:
	def __init__(self, board, size=4):
		self.size = size
		self.position = list()
		self.board = board


	def choose_starting_square(self):
		x, y = random.randrange(self.board.size), random.randrange(self.board.size)
		return x, y

	def disposition_horizontally(self, board):
		ship_placed = False
		while not ship_placed:
			self.position = list()
			cpt = 0
			x, y = self.choose_starting_square()
			while cpt + y < self.board.size and not self.board.array_occupied[x][y + cpt] and cpt < self.size:
				self.position.append((x, y + cpt))
				cpt = cpt + 1
			if cpt == self.size:
				ship_placed = True
		for x in self.position:
			self.board.array_occupied[x[0]][x[1]] = True

	def disposition_vertically(self, board):
		ship_placed = False
		while not ship_placed:
			self.position = list()
			cpt = 0
			x, y = self.choose_starting_square()
			while cpt + x < self.board.size and not self.board.array_occupied[x + cpt][y] and cpt < self.size:
				self.position.append((x + cpt, y))
				cpt = cpt + 1
			if cpt == self.size:
				ship_placed = True
		for x in self.position:
			self.board.array_occupied[x[0]][x[1]] = True


	def randomly_position_a_ship(self, board):
		# CHoose randomly a value between 0 and 1 to choose whether to place the boat vertically or horizontally
		position_number = random.randrange(2)
		if position_number == 0:
			self.disposition_horizontally(self.board)
		else :
			self.disposition_vertically(self.board)



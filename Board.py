#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""Board class - All functions relatives to the occupations of the board squares"""
import numpy
from tkinter import Frame, Canvas, BOTH


class Board(Frame):
	def __init__(self, size=8):
		super().__init__()
		self.size = size
		self.array_occupied = numpy.zeros((size, size), dtype=int)
		self.canvas = None
	# 	self.initUI()
	#
	# def initUI(self):
	# 	self.master.title("Battleship")
	# 	self.pack(fill=BOTH, expand=1)
	#
	# 	self.canvas = Canvas(self)
	# 	self.draw_board()
	# 	self.canvas.pack(fill=BOTH, expand=1)

	# def draw_board(self):
	# 	for x in range(self.size):
	# 		for y in range(self.size):
	# 			self.canvas.create_rectangle(x * 60 + 30, y * 60 + 30, x * 60 + 90, y * 60 + 90)

	def count_number_of_empty_square(self):
		return self.array_occupied.size - numpy.count_nonzero(self.array_occupied)

	def count_number_of_occupied_square(self):
		return numpy.count_nonzero(self.array_occupied)

	def occupy_area(self, ship_position, occupy_squares=1):
		occupied_area = set()
		for position in ship_position:
			x_list, y_list = [0, ], [0, ]
			x, y = position[0], position[1]
			if x > 0:
				x_list.append(-1)
			if y > 0:
				y_list.append(-1)
			if x < self.size - 1:
				x_list.append(1)
			if y < self.size - 1:
				y_list.append(1)
			for x_diff in x_list:
				for y_diff in y_list:
					occupied_area.add((x + x_diff, y + y_diff))

		for position in occupied_area:
			x, y = position[0], position[1]
			self.array_occupied[x][y] = self.array_occupied[x][y] + occupy_squares

	def is_positionning_possible(self, ship):
		ship_size = ship.size
		keep_going = True
		for i in range(self.size):
			for j in range(self.size):
				if not self.array_occupied[i][j] and (i, j) not in ship.forbidden_position:
					cpt = 1
					# Looking horizontally
					while keep_going and cpt < ship_size and i + cpt < self.size:
						if not self.array_occupied[i + cpt][j]:
							cpt += 1
						else:
							keep_going = False
							cpt = 1
					if cpt == ship_size:
						return True

					# Looking vertically
					keep_going = True
					while keep_going and cpt < ship_size and j + cpt < self.size:
						if not self.array_occupied[i][j + cpt]:
							cpt += 1
						else:
							keep_going = False
							cpt = 1
					if cpt == ship_size:
						return True
		return False







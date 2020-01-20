#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import random
import Board
from tkinter import Label, NW
from PIL import Image, ImageTk

size_to_ship = {1: 'battleships_img/submarine.png',
                2: 'battleships_img/torpedo.png',
                3: 'battleships_img/destroyer.png',
                4: 'battleships_img/escort.png'}


class Ship:
	def __init__(self, board, size=4):
		self.size = size
		self.position = list()
		self.board = board
		self.direction = None
		self.user_position = None

	def choose_starting_square(self):
		x, y = random.randrange(self.board.size), random.randrange(self.board.size)
		return x, y

	def disposition_horizontally(self, board):
		ship_placed = False
		while not ship_placed:
			self.position = list()
			cpt = 0
			x, y = self.choose_starting_square()
			while cpt + y < self.board.size and self.are_nearby_square_empty(x, y + cpt) and cpt < self.size:
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
			while cpt + x < self.board.size and self.are_nearby_square_empty(x + cpt, y) and cpt < self.size:
				self.position.append((x + cpt, y))
				cpt = cpt + 1
			if cpt == self.size:
				ship_placed = True
		for x in self.position:
			self.board.array_occupied[x[0]][x[1]] = True

	def randomly_position_a_ship(self):
		# CHoose randomly a value between 0 and 1 to choose whether to place the boat vertically or horizontally
		position_number = random.randrange(2)
		if position_number == 0:
			self.direction = 'horizontally'
			self.disposition_horizontally(self.board)
		else:
			self.direction = 'vertically'
			self.disposition_vertically(self.board)
		self.user_position = [(x[0] + 1, x[1] + 1) for x in self.position]

	def are_nearby_square_empty(self, position_x, position_y):
		# It's necessary to check what square we're going to inspect otherwise it can raise an IndexError
		square_to_inspect_x, square_to_inspect_y = [0,], [0,]
		if position_x > 0: square_to_inspect_x.append(-1)
		if position_y > 0: square_to_inspect_y.append(-1)
		if position_x < self.board.size - 1: square_to_inspect_x.append(1)
		if position_y < self.board.size - 1: square_to_inspect_y.append(1)
		for x_diff in square_to_inspect_x:
			for y_diff in square_to_inspect_y:
				try:
					if self.board.array_occupied[position_x + x_diff][position_y + y_diff]:
						return False
				except IndexError as e:
					print('AN ERROR HAS OCCURED')
		return True

	def draw_image(self, canvas):
		img_to_open = size_to_ship[self.size]
		battleship_img = Image.open(img_to_open)
		newsize = (60 * self.size, 60)
		battleship_img = battleship_img.resize(newsize)
		y_value = self.position[0][1]
		if self.size > 1 and self.direction == 'horizontally':
			battleship_img = battleship_img.transpose(Image.ROTATE_90)
			y_value = self.position[-1][1]
		photo = ImageTk.PhotoImage(battleship_img)
		canvas.create_image(30 + self.position[0][0] * 60, 450 - y_value * 60, image=photo, anchor=NW)
		label = Label(image=photo)
		label.image = photo  # keep a reference!

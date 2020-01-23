#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import random
from tkinter import Label, NW
from PIL import Image, ImageTk

# Affect pictures according to the ship sizes
size_to_ship = {1: 'battleships_img/submarine.png',
                2: 'battleships_img/torpedo.png',
                3: 'battleships_img/destroyer.png',
                4: 'battleships_img/escort.png'}


class Ship:

	def __init__(self, board, size=4):
		self.name = None
		self.size = size
		self.position = list()
		self.board = board
		self.direction = None
		self.user_position = None
		self.forbidden_position = list()

	def choose_starting_square(self):
		legal_position = False
		x, y = None, None
		while not legal_position:
			x, y = random.randrange(self.board.size), random.randrange(self.board.size)
			if (x, y) not in self.forbidden_position:
				legal_position = True
		return x, y

	def disposition_horizontally(self):
		self.position = list()
		cpt = 0
		x, y = self.choose_starting_square()
		while cpt + y < self.board.size and not self.board.array_occupied[x][y + cpt] and cpt < self.size:
			self.position.append((x, y + cpt))
			cpt = cpt + 1
		if cpt == self.size:
			return True
		return False

	def disposition_vertically(self):
		self.position = list()
		cpt = 0
		x, y = self.choose_starting_square()
		while cpt + x < self.board.size and not self.board.array_occupied[x + cpt][y] and cpt < self.size:
			self.position.append((x + cpt, y))
			cpt = cpt + 1
		if cpt == self.size:
			return True
		return False

	def randomly_position_a_ship(self):
		ship_placed = False
		# Choose randomly a value between 0 and 1 to choose whether to place the boat vertically or horizontally
		while len(self.position) < self.size and not ship_placed:
			position_number = random.randrange(2)
			if position_number == 0:
				self.direction = 'horizontally'
				ship_placed = self.disposition_horizontally()
			else:
				self.direction = 'vertically'
				ship_placed = self.disposition_vertically()
		self.board.occupy_area(self.position)
		self.user_position = [(x[0] + 1, x[1] + 1) for x in self.position]

	def remove_ship(self):
		self.board.occupy_area(self.position, occupy_squares=-1)
		self.direction = None
		self.position = list()
		self.user_position = None

	def draw_image(self, canvas):
		img_to_open = size_to_ship[self.size]
		battleship_img = Image.open(img_to_open)
		newsize = (60 * self.size, 60)
		battleship_img = battleship_img.resize(newsize)
		try:
			y_value = self.position[0][1]
		except IndexError as e:
			print(e)
		if self.size > 1 and self.direction == 'horizontally':
			battleship_img = battleship_img.transpose(Image.ROTATE_90)
			y_value = self.position[-1][1]
		photo = ImageTk.PhotoImage(battleship_img)
		canvas.create_image(30 + self.position[0][0] * 60,
		                    (60 * self.board.size - 30) - y_value * 60,
		                    image=photo,
		                    anchor=NW)
		label = Label(image=photo)
		label.image = photo

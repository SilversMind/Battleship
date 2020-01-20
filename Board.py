#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import numpy
from tkinter import Frame, Canvas, BOTH


class Board(Frame):
	def __init__(self, size=8):
		super().__init__()
		self.size = size
		self.array_occupied = numpy.zeros((size, size), dtype=bool)
		self.canvas = None
		self.initUI()

	def initUI(self):
		self.master.title("Battleship")
		self.pack(fill=BOTH, expand=1)

		self.canvas = Canvas(self)
		self.draw_board()
		#self.draw_image(self.canvas)
		self.canvas.pack(fill=BOTH, expand=1)

	def draw_board(self):
		for x in range(self.size):
			for y in range(self.size):
				self.canvas.create_rectangle(x * 60 + 30, y * 60 + 30, x * 60 + 90, y * 60 + 90)





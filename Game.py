#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""Game class - Manages all the positionning mechanism"""
import queue
import time
import sys


class Game:
	def __init__(self, board, ships):
		self.board = board
		self.ships = list(reversed(ships))
		self.placed = queue.LifoQueue(maxsize=len(self.ships))
		self.to_place = queue.LifoQueue(maxsize=len(self.ships))
		self.t0 = time.time()
		for ship in ships:
			self.to_place.put(ship)

	def find_ship_location(self, current_ship):
		# Heuristic function to reduce number of dead end obtained when trying
		# to place a ship using a naive random positionning algorithm.
		if self.board.is_positionning_possible(current_ship):
			current_ship.randomly_position_a_ship()
			self.placed.put(current_ship)
		else:
			self.to_place.put(current_ship)
			current_ship.forbidden_position = list()
			previous_ship = self.placed.get()
			previous_ship.forbidden_position.append(previous_ship.position[0])
			previous_ship.remove_ship()
			self.find_ship_location(previous_ship)

	def play(self):
		while not self.placed.full():
			if time.time() - self.t0 > 6:
				print('No solution found before timeout')
				sys.exit(-1)
			current_ship = self.to_place.get()
			self.find_ship_location(current_ship)

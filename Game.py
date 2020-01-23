#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import Ship
import Board
import queue

class Game:
	def __init__(self, board, ships):
		self.board = board
		self.ships = list(reversed(ships))
		self.placed = queue.LifoQueue(maxsize=len(self.ships))
		self.to_place = queue.LifoQueue(maxsize=len(self.ships))
		for ship in ships:
			self.to_place.put(ship)
	def find_ship_location(self, current_ship):
		# Heuristic function to reduce number of dead end obtained when trying
		# to place a ship using a naive random positionning algorithm.
		if self.board.is_positionning_possible(current_ship):
			# for x in self.placed.queue:
			# 	print(x.position)
			current_ship.randomly_position_a_ship()
			self.placed.put(current_ship)
		else:
			self.to_place.put(current_ship)
			current_ship.forbidden_position = list()
			previous_ship = self.placed.get()
			previous_ship.forbidden_position.append(previous_ship.position[0])
			previous_ship.remove_ship()
			self.find_ship_location(previous_ship)

	def main(self):
		while not self.placed.full():
			current_ship = self.to_place.get()
			self.find_ship_location(current_ship)

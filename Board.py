#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""
import numpy

class Board:
	def __init__(self, size=4):
		self.size = size
		self.array_occupied = numpy.zeros((size, size), dtype=bool)



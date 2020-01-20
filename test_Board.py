import unittest
from Board import *

b_test = Board(8)

class test_Board(unittest.TestCase):

	def test_size(self):
		assert b_test.size == 8

	def test_array(self):
		# Check matrix size and all elements value (supposed to be initialized to False)
		assert b_test.array_occupied.shape == (8, 8)
		assert not numpy.any(b_test.array)
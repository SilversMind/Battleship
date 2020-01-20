import unittest
import Ship
import Board

b_test = Board.Board(8)
ship_test = Ship.Ship(3)


class test_Board(unittest.TestCase):

	def test_size(self):
		assert ship_test.size == 3

	def test_choose_starting_square(self):
		starting_square = ship_test.choose_starting_square()
		assert len(starting_square) == 2
		assert all([True for x in starting_square if 0 < x < 8])

	def test_disposition(self):
		ship_test.disposition(b_test)
		assert len(ship_test.position) == 3
		# Check if the board are all along the same column
		assert len(set([x[0] for x in ship_test.position])) == 1
		# Check if the square are contiguous
		assert ([x[1] for x in ship_test.position] == list(range(ship_test.position[0][1], ship_test.position[0][1] + ship_test.size)))



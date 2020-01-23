import unittest
import Ship
import Board

board_test = Board.Board(8)
ship_test = Ship.Ship(board_test, 3)


class test_Board(unittest.TestCase):

	def test_size(self):
		assert ship_test.size == 3

	def test_choose_starting_square(self):
		starting_square = ship_test.choose_starting_square()
		assert len(starting_square) == 2
		assert all([True for x in starting_square if 0 < x < 8])

	def test_randomly_position_a_ship(self):
		ship_test.randomly_position_a_ship()
		assert len(ship_test.position) == 3
		# Check if the board are all along the same column
		assert len(set([x[1] for x in ship_test.position])) == 1 or len(set([x[0] for x in ship_test.position])) == 1
		# Check if the square are contiguous
		assert ([x[0] for x in ship_test.position] == list(
			range(ship_test.position[0][0], ship_test.position[0][0] + ship_test.size))) or (
				       [x[1] for x in ship_test.position] == list(
			       range(ship_test.position[0][1], ship_test.position[0][1] + ship_test.size)))

	def test_remove_ship(self):
		b_test = Board.Board(8)
		test_ship = Ship.Ship(b_test, 3)
		test_ship.randomly_position_a_ship()
		test_ship.remove_ship()
		assert b_test.count_number_of_empty_square() == b_test.size * b_test.size
		assert not test_ship.position
		assert not test_ship.user_position
		assert not test_ship.direction

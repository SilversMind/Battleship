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

	def test_disposition_horizontally(self):
		b_test = Board.Board(8)
		ship_test.disposition_horizontally(b_test)
		assert len(ship_test.position) == 3
		# Check if the board are all along the same row
		assert len(set([x[0] for x in ship_test.position])) == 1
		# Check if the square are contiguous
		assert ([x[1] for x in ship_test.position] == list(range(ship_test.position[0][1], ship_test.position[0][1] + ship_test.size)))

	def test_disposition_vertically(self):
		b_test = Board.Board(4)
		ship_test.disposition_vertically(b_test)
		assert len(ship_test.position) == 3
		# Check if the board are all along the same column
		assert len(set([x[1] for x in ship_test.position])) == 1
		# Check if the square are contiguous
		assert ([x[0] for x in ship_test.position] == list(range(ship_test.position[0][0], ship_test.position[0][0] + ship_test.size)))

	def test_position_multiple_ships(self):
		b_test = Board.Board(5)
		size_ship_to_place = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
		for x in size_ship_to_place:
			ship = Ship.Ship(b_test, x)
			ship.randomly_position_a_ship(b_test)
			# Check if the number of square occupied on the board is equal to the sum of the ships' size
			# i.e check if all the ships have been placed
		assert list(b_test.array_occupied.flatten()).count(True) == sum(size_ship_to_place)


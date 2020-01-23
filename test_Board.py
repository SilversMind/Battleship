import unittest
import Board
import Ship
import numpy

b_test = Board.Board(8)


class test_Board(unittest.TestCase):

	def test_size(self):
		assert b_test.size == 8

	def test_array(self):
		# Check matrix size and all elements value (supposed to be initialized to False)
		assert b_test.array_occupied.shape == (8, 8)
		assert not numpy.any(b_test.array_occupied)

	def test_occupy_area(self):
		b_test = Board.Board(4)
		ship = Ship.Ship(b_test, 3)
		ship.position = [(1, 0), (1, 1), (1, 2)]
		b_test.occupy_area(ship.position)
		assert not numpy.sum(ship.board.array_occupied > 1)

		ship2 = Ship.Ship(b_test, 3)
		ship2.position = [(1, 2), (1, 3)]
		b_test.occupy_area(ship2.position)

		assert numpy.sum(ship.board.array_occupied == 2) == 9

		ship2.remove_ship()

		assert not numpy.sum(ship.board.array_occupied > 1)

	def test_is_positionning_possible(self):
		b_test = Board.Board(4)
		ship_test = Ship.Ship(b_test, 3)
		assert b_test.is_positionning_possible(ship_test)

		b_test.array_occupied = numpy.ones((4, 4), dtype=int)
		b_test.array_occupied[0][3] = 0
		b_test.array_occupied[2][3] = 0
		assert not b_test.is_positionning_possible(ship_test)

		b_test.array_occupied[1][3] = 0
		assert b_test.is_positionning_possible(ship_test)

		ship_test.forbidden_position.append((0, 3))
		assert not b_test.is_positionning_possible(ship_test)



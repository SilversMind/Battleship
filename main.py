#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""[application description here]"""

from tkinter import Tk, Label
from PIL import ImageTk, Image
import Board, Ship


def main():

    root = Tk()
    root.geometry("543x540")
    board = Board.Board(8)
    size_ship_to_place = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
    for x in size_ship_to_place:
        ship = Ship.Ship(board, x)
        ship.randomly_position_a_ship()
        ship.draw_image(board.canvas)
        print(ship.user_position)
    root.mainloop()

if __name__ == '__main__':
    main()
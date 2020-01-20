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
    board = Board.Board()
    ship = Ship.Ship(board, 2)
    ship.randomly_position_a_ship()
    ship.draw_image(board.canvas)
    print(ship.user_position)
    root.mainloop()

if __name__ == '__main__':
    main()
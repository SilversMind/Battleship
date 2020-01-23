#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""Main Program"""

from tkinter import Tk
import Game
import Board
import Ship

def main():
    root = Tk()
    b_test = Board.Board(5)
    windows_size = (b_test.size + 1) * 60
    root.geometry("{0}x{0}".format(str(windows_size)))
    ships_size = (3, 3, 3, 3)
    ships = [Ship.Ship(b_test, x) for x in ships_size]
    game = Game.Game(b_test, ships)
    game.main()
    while not game.placed.empty():
        ship = game.placed.get()
        ship.draw_image(b_test.canvas)

    root.mainloop()


if __name__ == '__main__':
    main()
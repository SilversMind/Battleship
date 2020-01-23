#! /usr/bin/python
# -*- coding: utf-8 -*-
# Author: Samy Sidhoum
"""Main Program"""

import Game
import Board
import Ship
from tkinter import *
from tkinter.ttk import *


def init_interface(size=8, ships_size=None, game=None, default_ship_value = None):

    def draw_board_and_canvas(size):
        canvas = Canvas()
        for x in range(size):
            for y in range(size):
                canvas.create_rectangle(x * 60 + 30, y * 60 + 30, x * 60 + 90, y * 60 + 90)
        return canvas

    # creating main tkinter window/toplevel
    master = Tk()
    master.title('Battleship')
    # master.geometry("1000x1000")
    c = draw_board_and_canvas(size)
    c.config(width=(size + 1) * 60, height=(size + 1) * 60)
    c.grid(row=0, column=1)

    img = PhotoImage(file="battleships_img/escort.png")
    img1 = img.subsample(2, 2)
    img = PhotoImage(file="battleships_img/destroyer.png")
    img2 = img.subsample(3, 2)
    img = PhotoImage(file="battleships_img/torpedo.png")
    img3 = img.subsample(2, 2)
    img = PhotoImage(file="battleships_img/submarine.png")
    img4 = img.subsample(4, 2)

    # Set default value
    v_escort, v_destroyer, v_torpedo, v_submarine = StringVar(), StringVar(), StringVar(), StringVar()
    if default_ship_value:
        v_escort.set(str(default_ship_value[0]))
        v_destroyer.set(str(default_ship_value[1]))
        v_torpedo.set(str(default_ship_value[2]))
        v_submarine.set(str(default_ship_value[3]))
    else:
        v_escort.set("0")
        v_destroyer.set("0")
        v_torpedo.set("0")
        v_submarine.set("0")


    # setting image with the help of label
    Label(master, image=img1).grid(row=1, column=0, padx=5, pady=5)

    sb_escort = Spinbox(master, from_=0, to=10, textvariable=v_escort)
    sb_escort.grid(row=1, column=1)

    Label(master, image=img2).grid(row=2, column=0, padx=5, pady=5)

    sb_destroyer = Spinbox(master, from_=0, to=10, textvariable=v_destroyer)
    sb_destroyer.grid(row=2, column=1)

    Label(master, image=img3).grid(row=1, column=2, padx=5, pady=5)

    sb_torpedo = Spinbox(master, from_=0, to=10, textvariable=v_torpedo)
    sb_torpedo.grid(row=1, column=3)

    Label(master, image=img4).grid(row=2, column=2, padx=5, pady=5)

    sb_submarine = Spinbox(master, from_=0, to=10, textvariable=v_submarine)
    sb_submarine.grid(row=2, column=3)

    l1 = Label(master, text="Board size")
    l1.grid(row=3, column=0)

    v_boardsize = StringVar()
    v_boardsize.set("8")

    sb_boardsize = Spinbox(master, from_=0, to=10, textvariable=v_boardsize)
    sb_boardsize.grid(row=3, column=2, padx=5, pady=20)

    if ships_size:
        print(ships_size)

    def quit(master):
        master.destroy()

    def scramble_button():
        size_ = int(sb_boardsize.get())
        number_escort = sb_escort.get()
        number_destroyer = sb_destroyer.get()
        number_torpedo = sb_torpedo.get()
        number_submarine = sb_submarine.get()
        default_ship_value = (number_escort, number_destroyer, number_torpedo, number_submarine)

        ship_list = list()
        for cpt, number in enumerate((number_submarine, number_torpedo, number_destroyer, number_escort)):
            for x in range(int(number)):
                ship_list.append(cpt + 1)
        ships_size = list(reversed(ship_list))
        print(ship_list)
        b_test = Board.Board(size_)
        ships = [Ship.Ship(b_test, x) for x in ships_size]
        game = None
        if size_ > 1 and ships_size:
            game = Game.Game(b_test, ships)
            game.main()

        quit(master)
        init_interface(int(size_), ships_size, game, default_ship_value)

    board_scrambler = Button(master, text='Scramble', command=scramble_button)
    board_scrambler.grid(row=3, column=3)

    if game:
        while not game.placed.empty():
            ship = game.placed.get()
            ship.draw_image(c)

    mainloop()



def main():
    root = Tk()
    b_test = Board.Board(5)
    windows_size = (b_test.size + 1) * 60
    root.geometry("{0}x{0}".format(str(windows_size)))
    ships_size = ()
    ships = [Ship.Ship(b_test, x) for x in ships_size]
    game = Game.Game(b_test, ships)
    game.main()
    while not game.placed.empty():
        ship = game.placed.get()
        ship.draw_image(b_test.canvas)

    root.mainloop()


if __name__ == '__main__':
    # main()
    init_interface()
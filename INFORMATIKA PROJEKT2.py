import pygame
import math             #ubacio sam sve module potrebne za sada, još ću ih dodati 
import numpy as np

BROJ_RED = 6            # igra se odvija u tablici od 42 mjesta, raspoređenih
                        # u 6 redova i 7 stupaca
BROJ_STUPAC = 7


def create_board():                             # pomoću numpy-a kreiram array od kojem
    board = np.zeros((BROJ_RED, BROJ_STUPAC))   # 6 puta sedam mjesta ispunjenih nulama jer kasnije
    return board                                # pomoću toga mislim provjeravat pozicije novčića 

def print_board(board):
    print(board)

board = create_board()                          # stvaram "board"

print_board(board)                              # printam array od nula
                                                # to je to za sad, Sretan Uskrs ;)


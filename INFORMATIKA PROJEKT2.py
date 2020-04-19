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


def postavljanje_novčića(board, row, col, piece):  #ovdje imenujem "piece" koji će mi kasnije služiti kao pozicija novčiča
    board[row][col] = piece                        #to jest određuje je li novčić na određenoj poziciji 

                                                #ova cijela funkcija se odnosi na provjeravanje pobjedničkog poteza tj.
                                                #nalaze li se četiri novčića jedan za drugim

def pobjeda(board, piece):
    for i in range (BROJ_STUPAC - 3):
        for j in range (BROJ_RED):
            if board[i][j] == piece and board[i][j+1] == piece and board[i][j+2] == piece and board[i][j+3] == piece:   #ovdje provjeravam horizontalno
                return True
    for i in range (BROJ_STUPAC):
        for j in range (BROJ_RED - 3):
            if board[i][j] == piece and board[i+1][j] == piece and board[i+2][j] == piece and board[i+3][j] == piece:   #ovdje provejravam vertikalno
                return True
    for i in range (BROJ_STUPAC - 3):
        for j in range (BROJ_RED - 3):
            if board[i][j] == piece and board[i+1][j+1] == piece and board[i+2][j+2] == piece and board[i+3][j+3] == piece:  #ovdje provejravam jedne dijagonale
                return True
    for i in range (BROJ_STUPAC - 3):
        for j in range (3, BROJ_RED):
            if board[i][j] == piece and board[i-1][j+1] == piece and board[i-2][j+2] == piece and board[i-3][j+3] == piece:  #ovdje provjeravam druge dijagonale
                return True

PLAVO = (0, 0, 255)             #određujem boju te dimenzije boarda na screenu
CRNO = (0, 0, 0)                #širinu i visinu samoga screena
CRVENO = (255, 0, 0)            #te radijus novčića tj. mjesta gdje se novčići stavljaju
ŽUTO = (255, 255, 0)

VELIČINA = 100

ŠIRINA = BROJ_STUPAC * VELIČINA
VISINA = (BROJ_RED+1) * VELIČINA

size = (ŠIRINA, VISINA)

RADIUS = int(VELIČINA/2 - 5)

    
def crtaj_board(board):                                                                     #crtam board tako da u plavom pravokutniku radim crne rupe u
    for i in range (BROJ_STUPAC):                                                           #u obliku kružnica (mjesta gdje će novčići "upadati")
        for j in range (BROJ_RED):
            pygame.draw.rect(screen, PLAVO, (i*VELIČINA, (j+1)*VELIČINA, VELIČINA, VELIČINA))
            pygame.draw.circle(screen, CRNO, (int(i*VELIČINA+VELIČINA/2), int(j*VELIČINA+VELIČINA+VELIČINA/2)), RADIUS)
    pygame.display.update()

screen = pygame.display.set_mode(size)      #stvaram screen u pygame-u
crtaj_board(board)                          #crtam board u screenu
pygame.display.update()

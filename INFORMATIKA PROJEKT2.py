import pygame
import math             #ubacio sam sve module potrebne za sada, još ću ih dodati 
import numpy as np
import sys

BROJ_RED = 6            # igra se odvija u tablici od 42 mjesta, raspoređenih
                        # u 6 redova i 7 stupaca
BROJ_STUPAC = 7


def create_board():                             # pomoću numpy-a kreiram array od kojem
    board = np.zeros((BROJ_RED, BROJ_STUPAC))   # 6 puta sedam mjesta ispunjenih nulama jer kasnije
    return board                                # pomoću toga mislim provjeravat pozicije novčića 

def print_board(board):
    print(np.flip(board, 0))

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
            if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:   #ovdje provjeravam horizontalno
                return True
    for i in range (BROJ_STUPAC):
        for j in range (BROJ_RED - 3):
            if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:   #ovdje provejravam vertikalno
                return True
    for i in range (BROJ_STUPAC - 3):
        for j in range (BROJ_RED - 3):
            if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:  #ovdje provejravam jedne dijagonale
                return True
    for i in range (BROJ_STUPAC - 3):
        for j in range (3, BROJ_RED):
            if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:  #ovdje provjeravam druge dijagonale
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

    
def crtaj_board(board):
	for i in range(BROJ_STUPAC):                                                                                                #crtam board tako da u plavom praovkutniku radim crne rupe u 
		for j in range(BROJ_RED):                                                                                           #obliku kružnica (mjesta gdje će novčići "upadati")
			pygame.draw.rect(screen, PLAVO, (i*VELIČINA, (j+1)*VELIČINA, VELIČINA, VELIČINA))                           
			pygame.draw.circle(screen, CRNO, (int(i*VELIČINA+VELIČINA/2), int(j*VELIČINA+VELIČINA+VELIČINA/2)), RADIUS)
	
	for i in range(BROJ_STUPAC):
		for j in range(BROJ_RED):		
			if board[j][i] == 1:                                                                                                    #kasnije sam u programu napravio da potez jednog igrača pušta trag
				pygame.draw.circle(screen, CRVENO, (int(i*VELIČINA+VELIČINA/2), VISINA-int(j*VELIČINA+VELIČINA/2)), RADIUS)     #u obliku broja 1, a drugi u obliku broja 2 ; s obzirom čiji je potez
			elif board[j][i] == 2:                                                                                                  #crtam novčiće u njegovoj boji 
				pygame.draw.circle(screen, ŽUTO, (int(i*VELIČINA+VELIČINA/2), VISINA-int(j*VELIČINA+VELIČINA/2)), RADIUS)
	pygame.display.update()
     

screen = pygame.display.set_mode(size)      #stvaram screen u pygame-u
crtaj_board(board)                          #crtam board u screenu
pygame.display.update()



def dobra_pozicija(board, col):                 #ovime određujem je li pozicija slobodna tj. nalazim stupac gdje novčić upada
	return board[BROJ_RED - 1][col] == 0

def slj_otvoren_red(board, col):
	for i in range(BROJ_RED):               #ovdje nalazim na kojem mjestu u tom stupcu pada novčić (koji red)
		if board[i][col] == 0:
			return i

game_over = False
potez = 0                                       # sve je spremno za foto finish i pokretanje igre, potez je postavljen na 0, a kasnije se
pygame.init()                                   # mijenja jednom po svakom potezu (između 0 i 1)

myfont = pygame.font.SysFont("monospace", 40)

while not game_over:                            #pokrećem glavni program dok igra traje

	for event in pygame.event.get():
		if event.type == pygame.QUIT:   #gasi sve
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, CRNO, (0,0, ŠIRINA, VELIČINA))                             #ovdje definiram što je na screenu kada
			posx = event.pos[0]                                                                 #netko pomiče mouse te ovisno čiji je potez
			if potez == 0:                                                                      #dolazi crveni ili žuti krug iznad cijelog
				pygame.draw.circle(screen, CRVENO, (posx, int(VELIČINA/2)), RADIUS)         #boarda 
			else: 
				pygame.draw.circle(screen, ŽUTO, (posx, int(VELIČINA/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:                        #definiram što se događa kod kilika mišem s obzirom čiji je potez
			pygame.draw.rect(screen, CRNO, (0,0, ŠIRINA, VELIČINA))
			if potez == 0:                                          #prvi igrač na redu
				posx = event.pos[0]
				col = int(math.floor(posx/VELIČINA))            #vraća najmanji cijeli broj koji je manji ili jednak rezultatu dijeljenja čime
                                                                                #odredi u koji stupac želim staviti novčić
				if dobra_pozicija(board, col):
					row = slj_otvoren_red(board, col)        #u stupac koji smo odredili te u prvi slobodni red se postavlja novčić koji ostavlja
					postavljanje_novčića(board, row, col, 1) #trag 1 što će u crtaj_board() značiti da ide crveni novčić

					if pobjeda(board, 1):                                                       #u slučaju pobjede crvenog (4 novčića)
						natpis = myfont.render("Jedinica pobjedila kume!!", 1, CRVENO)      #preko screena se pojavljuje poruka
						screen.blit(natpis, (40,10))                                        #te se igra zasutavlja
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]                                                 #sve isto samo u slučaju kad je drugi igrač na potezu
				col = int(math.floor(posx/VELIČINA))                                #naš novčić ostavlja trag 2 što znači da u crtaj_board()
                                                                                                    #se na screenu na tom mjestu crta žuti novčić   
				if dobra_pozicija(board, col):
					row = slj_otvoren_red(board, col)
					postavljanje_novčića(board, row, col, 2)

					if pobjeda(board, 2):
						natpis = myfont.render("Dvojka odnijela sve kume!!", 1, ŽUTO)  #u slučaju pobjede žutog natpis se promijeni
						screen.blit(natpis, (40,10))                                   #te je on preko ekrana
						game_over = True                                               #igra također završava 

			print_board(board)    #nakon svakog poteza se u IDLE printa array, a na screenu se pojavljuju novčići ovisno o našem odabiru
			crtaj_board(board)

			potez += 1            #pomoću ove jednostavne "petlje" izmijenjujemo poteze prvog i drugog igrača
			potez = potez % 2

			if game_over:               #gejm over
				pygame.time.wait(100)

import pygame, sys
from pygame.locals import *

# colors
BACKGROUND = (255, 255, 255)
BLACKSQUARES = (209, 139, 71)
WHITESQUARES = (255, 206, 158)
MOVETOSQUARES = (255, 0, 0)
MOVEFROMSQUARES = (0, 0, 255)

# board info
BOARD = pygame.Rect(20, 20, 260, 260)
X_SQUARES = 8
Y_SQUARES = 8
DELTA_X = BOARD.width/X_SQUARES
DELTA_Y = BOARD.height/Y_SQUARES

# piece images
WPAWN = pygame.image.load('sprites/wpawn.png')
WKNIGHT = pygame.image.load('sprites/wknight.png')
WBISHOP = pygame.image.load('sprites/wbishop.png')
WROOK = pygame.image.load('sprites/wrook.png')
WQUEEN = pygame.image.load('sprites/wqueen.png')
WKING = pygame.image.load('sprites/wking.png')
WPAWN = pygame.transform.smoothscale(WPAWN, (DELTA_X, DELTA_Y))
WKNIGHT = pygame.transform.smoothscale(WKNIGHT, (DELTA_X, DELTA_Y))
WBISHOP = pygame.transform.smoothscale(WBISHOP, (DELTA_X, DELTA_Y))
WROOK = pygame.transform.smoothscale(WROOK, (DELTA_X, DELTA_Y))
WQUEEN = pygame.transform.smoothscale(WQUEEN, (DELTA_X, DELTA_Y))
WKING = pygame.transform.smoothscale(WKING, (DELTA_X, DELTA_Y))
BPAWN = pygame.image.load('sprites/bpawn.png')
BKNIGHT = pygame.image.load('sprites/bknight.png')
BBISHOP = pygame.image.load('sprites/bbishop.png')
BROOK = pygame.image.load('sprites/brook.png')
BQUEEN = pygame.image.load('sprites/bqueen.png')
BKING = pygame.image.load('sprites/bking.png')
BPAWN = pygame.transform.smoothscale(BPAWN, (DELTA_X, DELTA_Y))
BKNIGHT = pygame.transform.smoothscale(BKNIGHT, (DELTA_X, DELTA_Y))
BBISHOP = pygame.transform.smoothscale(BBISHOP, (DELTA_X, DELTA_Y))
BROOK = pygame.transform.smoothscale(BROOK, (DELTA_X, DELTA_Y))
BQUEEN = pygame.transform.smoothscale(BQUEEN, (DELTA_X, DELTA_Y))
BKING = pygame.transform.smoothscale(BKING, (DELTA_X, DELTA_Y))

# pieceArray contains location of pieces
pieceArray = [ [0]*X_SQUARES for _ in range(Y_SQUARES) ]
# movesArray contains current possible moves
movesArray = [ [0]*X_SQUARES for _ in range(Y_SQUARES) ]

# testing values
movesArray[3][0] = 1
movesArray[0][1] = -1
pieceArray[0][3] = 3
pieceArray[3][0] = 1
# end testing values

# converts num to sprite
def piece(num):
	if num == 1:
		return WPAWN
	elif num == 2:
		return WKNIGHT
	elif num == 3:
		return WBISHOP
	elif num == 4:
		return WROOK
	elif num == 5:
		return WQUEEN
	elif num == 6:
		return WKING
	elif num == -1:
		return BPAWN
	elif num == -2:
		return BKNIGHT
	elif num == -3:
		return BBISHOP
	elif num == -4:
		return BROOK
	elif num == -5:
		return BQUEEN
	elif num == -6:
		return BKING

# draws board
def drawBoard(surface, where, color):
	if color == 0:
		pygame.draw.rect(surface, WHITESQUARES, where + (DELTA_X, DELTA_Y))
	else:
		pygame.draw.rect(surface, BLACKSQUARES, where + (DELTA_X, DELTA_Y))

# draws highlight squares (current selected piece and possible moves)
def drawHighlights(surface, where, move):
	if move == 1:
		pygame.draw.rect(surface, MOVETOSQUARES, where + (DELTA_X, DELTA_Y))
	elif move == -1:
		pygame.draw.rect(surface, MOVEFROMSQUARES, where + (DELTA_X, DELTA_Y))

# draws pieces
def drawPieces(surface, where, pieceNum):
	if pieceNum > 0:
		surface.blit(piece(pieceNum), where)

# initializes game
def game_init():
	pygame.init()
	display = pygame.display.set_mode((300, 300))
	pygame.display.set_caption('Self-Modifying Chess')
	return display

# main loop
def game_main_loop(display):
	while True:
		display.fill(BACKGROUND)
		for i in range(X_SQUARES):
			for j in range(Y_SQUARES):
				here = (BOARD.left + i*DELTA_X, BOARD.top + j*DELTA_Y)
				drawBoard(display, here, (i+j)%2)
				drawHighlights(display, here,  movesArray[i][j])
				drawPieces(display, here, pieceArray[i][j])
		pygame.display.update()
	
		for event in pygame.event.get():
			#print(event)
			if event.type == QUIT:
				game_quit()

# quits game
def game_quit():
	pygame.quit()
	sys.exit()

DISPLAYSURF = game_init()
game_main_loop(DISPLAYSURF)

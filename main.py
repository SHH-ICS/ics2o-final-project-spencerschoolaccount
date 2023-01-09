import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
backgroundColour = (123,78,2)
playMat = (183,149,98)

opponentCardY = 30
playerCardY = 262
cardWidth = 148
cardHeight = 222

displayWidth = 1280
displayHeight = 720

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Kartice')

def gameloop():
	handSlot1 = (False, (x: )
	handSlot2 = False
	handSlot3 = False
	handSlot4 = False
	handSlot5 = False
	handSlot6 = False
	
	gameExit = False
	while not gameExit:
		gameDisplay.fill(backgroundColour)
		pygame.draw.rect(gameDisplay, playMat, (240,20,800,474))
		pygame.draw.rect(gameDisplay, backgroundColour, (250,opponentCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (408,opponentCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (566,opponentCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (724,opponentCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (882,opponentCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (250,playerCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (408,playerCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (566,playerCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (724,playerCardY,cardWidth,cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (882,playerCardY,cardWidth,cardHeight))
		pygame.display.update()

gameloop()
import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
backgroundColour = (123,78,2)
playMat = (183,149,98)

cardWidth = 124
cardHeight = 181
opponentCardY = 51
playerCardY = opponentCardY + cardHeight + 50

displayWidth = 1280
displayHeight = 720

handSpacing = 10
playSpacing = 20

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Kartice')

def gameloop():
	handSlot1 = (False, 243, displayHeight - (cardHeight + 22))
	handSlot2 = (False, handSlot1[1] + cardWidth + handSpacing, handSlot1[2])
	handSlot3 = (False, handSlot2[1] + cardWidth + handSpacing, handSlot1[2])
	handSlot4 = (False, handSlot3[1] + cardWidth + handSpacing, handSlot1[2])
	handSlot5 = (False, handSlot4[1] + cardWidth + handSpacing, handSlot1[2])
	handSlot6 = (False, handSlot5[1] + cardWidth + handSpacing, handSlot1[2])

	playSlot1 = (False, 290)
	playSlot2 = (False, playSlot1[1] + cardWidth + playSpacing)
	playSlot3 = (False, playSlot2[1] + cardWidth + playSpacing)
	playSlot4 = (False, playSlot3[1] + cardWidth + playSpacing)
	playSlot5 = (False, playSlot4[1] + cardWidth + playSpacing)

	opponentSlot1 = (False, playSlot1[1])
	opponentSlot2 = (False, playSlot2[1])
	opponentSlot3 = (False, playSlot3[1])
	opponentSlot4 = (False, playSlot4[1])
	opponentSlot5 = (False, playSlot5[1])
	
	gameExit = False
	while not gameExit:
		gameDisplay.fill(backgroundColour)
		pygame.draw.rect(gameDisplay, playMat, (240,20,800,474))
		
		pygame.draw.rect(gameDisplay, backgroundColour, (opponentSlot1[1], opponentCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (opponentSlot2[1], opponentCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (opponentSlot3[1], opponentCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (opponentSlot4[1], opponentCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (opponentSlot5[1], opponentCardY, cardWidth, cardHeight))
		
		pygame.draw.rect(gameDisplay, backgroundColour, (playSlot1[1], playerCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (playSlot2[1], playerCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (playSlot3[1], playerCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (playSlot4[1], playerCardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, backgroundColour, (playSlot5[1], playerCardY, cardWidth, cardHeight))

		pygame.draw.rect(gameDisplay, backgroundColour, (1098, 360, cardWidth, cardHeight))

		if handSlot1:
			pygame.draw.rect(gameDisplay, red, (handSlot1[1], handSlot1[2], cardWidth, cardHeight))
		if handSlot2:
			pygame.draw.rect(gameDisplay, red, (handSlot2[1], handSlot2[2], cardWidth, cardHeight))
		if handSlot3:
			pygame.draw.rect(gameDisplay, red, (handSlot3[1], handSlot3[2], cardWidth, cardHeight))
		if handSlot4:
			pygame.draw.rect(gameDisplay, red, (handSlot4[1], handSlot4[2], cardWidth, cardHeight))
		if handSlot5:
			pygame.draw.rect(gameDisplay, red, (handSlot5[1], handSlot5[2], cardWidth, cardHeight))
		if handSlot6:
			pygame.draw.rect(gameDisplay, red, (handSlot6[1], handSlot6[2], cardWidth, cardHeight))
		
		pygame.display.update()

gameloop()
import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pink = (255, 133, 239)
green = (0,255,0)
blue = (0,0,255)
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

discardX = 58
discardY = 360

pileX = 1098
pileY = 360

endTurnX = 1098
endTurnY = pileY - cardWidth - 100

FPS = 30

font = pygame.font.SysFont(None, 25)

fullHandMessageTime = 0

cards = {
	"Grud": [1, 2, 1, blue],
	"LiterallyJustABear": [3, 4, 3, red],
	"Ferret": [1, 3, 2, green],
	"RatsRatsWe'reTheRats": [3, 1, 2, pink]
}

tempCardIDList = ['none']
for key in cards.keys():
	tempCardIDList.append(key)

cardIDs = tuple(tempCardIDList)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Kartice')

clock = pygame.time.Clock()

def drawcard(slot, isHandSlot=False):
	pygame.draw.rect(gameDisplay, cards[slot[0]][3], (slot[1], slot[2], cardWidth, cardHeight))
	if isHandSlot:
		messagetoscreen(str(cards[slot[0]][0]), x=slot[1], y=slot[2] + cardHeight/2)
		messagetoscreen(str(cards[slot[0]][1]), x=slot[1] + cardWidth - handSpacing, y=slot[2] + cardHeight/2)
	else:
		messagetoscreen(str(slot[3]), x=slot[1], y=slot[2] + cardHeight/2)
		messagetoscreen(str(slot[4]), x=slot[1] + cardWidth - handSpacing, y=slot[2] + cardHeight/2)

def messagetoscreen(msg,colour = white, size = 25, x=0,y=0):
	textSurf= font.render(msg, True, colour)
	gameDisplay.blit(textSurf,(x,y))

def gameloop():
	global fullHandMessageTime
	handSlot1 = [cardIDs[0], 243, displayHeight - (cardHeight + 22)]
	handSlot2 = [cardIDs[0], handSlot1[1] + cardWidth + handSpacing, handSlot1[2], 0]
	handSlot3 = [cardIDs[0], handSlot2[1] + cardWidth + handSpacing, handSlot1[2], 0]
	handSlot4 = [cardIDs[0], handSlot3[1] + cardWidth + handSpacing, handSlot1[2], 0]
	handSlot5 = [cardIDs[0], handSlot4[1] + cardWidth + handSpacing, handSlot1[2], 0]
	handSlot6 = [cardIDs[0], handSlot5[1] + cardWidth + handSpacing, handSlot1[2], 0]

	playSlot1 = [cardIDs[0], 290, playerCardY, 0, 0]
	playSlot2 = [cardIDs[0], playSlot1[1] + cardWidth + playSpacing, playerCardY, 0, 0]
	playSlot3 = [cardIDs[0], playSlot2[1] + cardWidth + playSpacing, playerCardY, 0, 0]
	playSlot4 = [cardIDs[0], playSlot3[1] + cardWidth + playSpacing, playerCardY, 0, 0]
	playSlot5 = [cardIDs[0], playSlot4[1] + cardWidth + playSpacing, playerCardY, 0, 0]

	opponentSlot1 = [cardIDs[0], playSlot1[1], opponentCardY, 0, 0]
	opponentSlot2 = [cardIDs[0], playSlot2[1], opponentCardY, 0, 0]
	opponentSlot3 = [cardIDs[0], playSlot3[1], opponentCardY, 0, 0]
	opponentSlot4 = [cardIDs[0], playSlot4[1], opponentCardY, 0, 0]
	opponentSlot5 = [cardIDs[0], playSlot5[1], opponentCardY, 0, 0]

	discardMode = False
	handSlots = ('none','handSlot1','handSlot2','handSlot3','handSlot4','handSlot5','handSlot6')
	playMode = handSlots[0]

	def drawUI():
		global fullHandMessageTime
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

		pygame.draw.rect(gameDisplay, blue, (pileX, pileY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, green, (discardX, discardY, cardWidth, cardHeight))
		pygame.draw.rect(gameDisplay, red, (endTurnX, endTurnY, cardWidth, cardWidth))

		if handSlot1[0] != cardIDs[0]:
			drawcard(handSlot1, True)
		if handSlot2[0] != cardIDs[0]:
			drawcard(handSlot2, True)
		if handSlot3[0] != cardIDs[0]:
			drawcard(handSlot3, True)
		if handSlot4[0] != cardIDs[0]:
			drawcard(handSlot4, True)
		if handSlot5[0] != cardIDs[0]:
			drawcard(handSlot5, True)
		if handSlot6[0] != cardIDs[0]:
			drawcard(handSlot6, True)

		if playSlot1[0] != cardIDs[0]:
			drawcard(playSlot1)
		if playSlot2[0] != cardIDs[0]:
			drawcard(playSlot2)
		if playSlot3[0] != cardIDs[0]:
			drawcard(playSlot3)
		if playSlot4[0] != cardIDs[0]:
			drawcard(playSlot4)
		if playSlot5[0] != cardIDs[0]:
			drawcard(playSlot5)

		if opponentSlot1[0] != cardIDs[0]:
			drawcard(opponentSlot1)
		if opponentSlot2[0] != cardIDs[0]:
			drawcard(opponentSlot2)
		if opponentSlot3[0] != cardIDs[0]:
			drawcard(opponentSlot3)
		if opponentSlot4[0] != cardIDs[0]:
			drawcard(opponentSlot4)
		if opponentSlot5[0] != cardIDs[0]:
			drawcard(opponentSlot5)

		if fullHandMessageTime > 0:
			messagetoscreen("Discard or play card before drawing another")
			fullHandMessageTime -= 1
		
		pygame.display.update()
	
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			elif event.type == pygame.MOUSEBUTTONUP:
				if not discardMode and playMode == handSlots[0]:
					if event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[0] in range(pileX,pileX+cardWidth) and pygame.mouse.get_pos()[1] in range(pileY, pileY+cardHeight):
						for i in range(1,7):
							if locals()['handSlot' + str(i)][0] == cardIDs[0]:
								locals()['handSlot' + str(i)][0] = cardIDs[random.randint(1,len(cardIDs)-1)]
								break
							else:
								if i == 6:
									fullHandMessageTime = 2 * FPS
	
					elif event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[0] in range(discardX,discardX+cardWidth) and pygame.mouse.get_pos()[1] in range(discardY, discardY+cardHeight):
						discardMode = True

					elif event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[0] in range(handSlot1[1],handSlot6[1] + cardWidth) and pygame.mouse.get_pos()[1] in range(handSlot1[2], handSlot1[2] + cardHeight):
						mouseX = pygame.mouse.get_pos()[0]
						mouseY = pygame.mouse.get_pos()[1]
						if mouseX in range(handSlot1[1],handSlot1[1] + cardWidth) and handSlot1[0] != cardIDs[0]:
							playMode = handSlots[1]
							
						elif mouseX in range(handSlot2[1],handSlot2[1] + cardWidth) and handSlot2[0] != cardIDs[0]:
							playMode = handSlots[2]

						elif mouseX in range(handSlot3[1],handSlot3[1] + cardWidth) and handSlot3[0] != cardIDs[0]:
							playMode = handSlots[3]

						elif mouseX in range(handSlot4[1],handSlot4[1] + cardWidth) and handSlot4[0] != cardIDs[0]:
							playMode = handSlots[4]

						elif mouseX in range(handSlot5[1],handSlot5[1] + cardWidth) and handSlot5[0] != cardIDs[0]:
							playMode = handSlots[5]

						elif mouseX in range(handSlot6[1],handSlot6[1] + cardWidth) and handSlot6[0] != cardIDs[0]:
							playMode = handSlots[6]
				
				elif playMode != handSlots[0]:
					if event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[1] in range(playerCardY,playerCardY+cardHeight):
						mouseX = pygame.mouse.get_pos()[0]
						mouseY = pygame.mouse.get_pos()[1]
						if mouseX in range(playSlot1[1],playSlot1[1]+cardWidth) and playSlot1[0] == cardIDs[0]:
							playSlot1[0] = locals()[playMode][0]
							playSlot1[3] = cards[locals()[playMode][0]][0]
							playSlot1[4] = cards[locals()[playMode][0]][1]
							print(playSlot1)
							locals()[playMode][0] = cardIDs[0]
							playMode = handSlots[0]
						
						elif mouseX in range(playSlot2[1],playSlot2[1]+cardWidth) and playSlot2[0] == cardIDs[0]:
							playSlot2[0] = locals()[playMode][0]
							playSlot2[3] = cards[locals()[playMode][0]][0]
							playSlot2[4] = cards[locals()[playMode][0]][1]
							print(playSlot2)
							locals()[playMode][0] = cardIDs[0]
							playMode = handSlots[0]
						
						elif mouseX in range(playSlot3[1],playSlot3[1]+cardWidth) and playSlot3[0] == cardIDs[0]:
							playSlot3[0] = locals()[playMode][0]
							playSlot3[3] = cards[locals()[playMode][0]][0]
							playSlot3[4] = cards[locals()[playMode][0]][1]
							print(playSlot3)
							locals()[playMode][0] = cardIDs[0]
							playMode = handSlots[0]
						
						elif mouseX in range(playSlot4[1],playSlot4[1]+cardWidth) and playSlot4[0] == cardIDs[0]:
							playSlot4[0] = locals()[playMode][0]
							playSlot4[3] = cards[locals()[playMode][0]][0]
							playSlot4[4] = cards[locals()[playMode][0]][1]
							print(playSlot4)
							locals()[playMode][0] = cardIDs[0]
							playMode = handSlots[0]
						
						elif mouseX in range(playSlot5[1],playSlot5[1]+cardWidth) and playSlot5[0] == cardIDs[0]:
							playSlot5[0] = locals()[playMode][0]
							playSlot5[3] = cards[locals()[playMode][0]][0]
							playSlot5[4] = cards[locals()[playMode][0]][1]
							print(playSlot5)
							locals()[playMode][0] = cardIDs[0]
							playMode = handSlots[0]

					elif event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[0] in range(locals()[playMode][1],locals()[playMode][1]+cardWidth) and pygame.mouse.get_pos()[1] in range(locals()[playMode][2],locals()[playMode][2]+cardHeight):
						playMode = handSlots[0]
						
				else:
					if event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[0] in range(discardX,discardX+cardWidth) and pygame.mouse.get_pos()[1] in range(discardX, discardX+cardHeight):
						discardMode = False
						
					elif event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[0] in range(handSlot1[1],handSlot6[1] + cardWidth) and pygame.mouse.get_pos()[1] in range(handSlot1[2], handSlot1[2] + cardHeight):
						mouseX = pygame.mouse.get_pos()[0]
						mouseY = pygame.mouse.get_pos()[1]
						if mouseX in range(handSlot1[1],handSlot1[1] + cardWidth) and handSlot1[0] != cardIDs[0]:
							handSlot1[0] = cardIDs[0]
							discardMode = False
							
						elif mouseX in range(handSlot2[1],handSlot2[1] + cardWidth) and handSlot2[0] != cardIDs[0]:
							handSlot2[0] = cardIDs[0]
							discardMode = False

						elif mouseX in range(handSlot3[1],handSlot3[1] + cardWidth) and handSlot3[0] != cardIDs[0]:
							handSlot3[0] = cardIDs[0]
							discardMode = False

						elif mouseX in range(handSlot4[1],handSlot4[1] + cardWidth) and handSlot4[0] != cardIDs[0]:
							handSlot4[0] = cardIDs[0]
							discardMode = False

						elif mouseX in range(handSlot5[1],handSlot5[1] + cardWidth) and handSlot5[0] != cardIDs[0]:
							handSlot5[0] = cardIDs[0]
							discardMode = False

						elif mouseX in range(handSlot6[1],handSlot6[1] + cardWidth) and handSlot6[0] != cardIDs[0]:
							handSlot6[0] = cardIDs[0]
							discardMode = False

					elif event.button == pygame.BUTTON_LEFT and pygame.mouse.get_pos()[1] in range(playerCardY,playerCardY+cardHeight):
						mouseX = pygame.mouse.get_pos()[0]
						mouseY = pygame.mouse.get_pos()[1]
						if mouseX in range(playSlot1[1],playSlot1[1]+cardWidth) and playSlot1[0]:
							playSlot1[0] = cardIDs[0]
							discardMode = False
						
						elif mouseX in range(playSlot2[1],playSlot2[1]+cardWidth) and playSlot2[0]:
							playSlot2[0] = cardIDs[0]
							discardMode = False
						
						elif mouseX in range(playSlot3[1],playSlot3[1]+cardWidth) and playSlot3[0]:
							playSlot3[0] = cardIDs[0]
							discardMode = False
						
						elif mouseX in range(playSlot4[1],playSlot4[1]+cardWidth) and playSlot4[0]:
							playSlot4[0] = cardIDs[0]
							discardMode = False
						
						elif mouseX in range(playSlot5[1],playSlot5[1]+cardWidth) and playSlot5[0]:
							playSlot5[0] = cardIDs[0]
							discardMode = False
		
		drawUI()
		clock.tick(FPS)

gameloop()

pygame.quit()
quit()

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

def messagetoscreen(msg,colour = white, size = 25, x=0,y=0):
	textSurf= font.render(msg, True, colour)
	gameDisplay.blit(textSurf,(x,y))

def gameloop():
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

	fullHandMessageTime = 0
	discardMode = False
	handSlots = ('none','handSlot1','handSlot2','handSlot3','handSlot4','handSlot5','handSlot6')
	playMode = handSlots[0]
	
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
			pygame.draw.rect(gameDisplay, cards[handSlot1[0]][3], (handSlot1[1], handSlot1[2], cardWidth, cardHeight))
			messagetoscreen(str(cards[handSlot1[0]][0]), x=handSlot1[1], y=handSlot1[2] + cardHeight/2)
			messagetoscreen(str(cards[handSlot1[0]][1]), x=handSlot1[1] + cardWidth - handSpacing, y=handSlot1[2] + cardHeight/2)
		if handSlot2[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[handSlot2[0]][3], (handSlot2[1], handSlot2[2], cardWidth, cardHeight))
			messagetoscreen(str(cards[handSlot2[0]][0]), x=handSlot2[1], y=handSlot2[2] + cardHeight/2)
			messagetoscreen(str(cards[handSlot2[0]][1]), x=handSlot2[1] + cardWidth - handSpacing, y=handSlot2[2] + cardHeight/2)
		if handSlot3[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[handSlot3[0]][3], (handSlot3[1], handSlot3[2], cardWidth, cardHeight))
			messagetoscreen(str(cards[handSlot3[0]][0]), x=handSlot3[1], y=handSlot3[2] + cardHeight/2)
			messagetoscreen(str(cards[handSlot3[0]][1]), x=handSlot3[1] + cardWidth - handSpacing, y=handSlot3[2] + cardHeight/2)
		if handSlot4[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[handSlot4[0]][3], (handSlot4[1], handSlot4[2], cardWidth, cardHeight))
			messagetoscreen(str(cards[handSlot4[0]][0]), x=handSlot4[1], y=handSlot4[2] + cardHeight/2)
			messagetoscreen(str(cards[handSlot4[0]][1]), x=handSlot4[1] + cardWidth - handSpacing, y=handSlot4[2] + cardHeight/2)
		if handSlot5[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[handSlot5[0]][3], (handSlot5[1], handSlot5[2], cardWidth, cardHeight))
			messagetoscreen(str(cards[handSlot5[0]][0]), x=handSlot5[1], y=handSlot5[2] + cardHeight/2)
			messagetoscreen(str(cards[handSlot5[0]][1]), x=handSlot5[1] + cardWidth - handSpacing, y=handSlot5[2] + cardHeight/2)
		if handSlot6[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[handSlot6[0]][3], (handSlot6[1], handSlot6[2], cardWidth, cardHeight))
			messagetoscreen(str(cards[handSlot6[0]][0]), x=handSlot6[1], y=handSlot6[2] + cardHeight/2)
			messagetoscreen(str(cards[handSlot6[0]][1]), x=handSlot6[1] + cardWidth - handSpacing, y=handSlot6[2] + cardHeight/2)
			
		if playSlot1[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[playSlot1[0]][3], (playSlot1[1], playerCardY, cardWidth, cardHeight))
			messagetoscreen(str(playSlot1[3]), x=playSlot1[1], y=playSlot1[2] + cardHeight/2)
			messagetoscreen(str(playSlot1[4]), x=playSlot1[1] + cardWidth - handSpacing, y=playSlot1[2] + cardHeight/2)
		if playSlot2[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[playSlot2[0]][3], (playSlot2[1], playerCardY, cardWidth, cardHeight))
			messagetoscreen(str(playSlot2[3]), x=playSlot2[1], y=playSlot2[2] + cardHeight/2)
			messagetoscreen(str(playSlot2[4]), x=playSlot2[1] + cardWidth - handSpacing, y=playSlot2[2] + cardHeight/2)
		if playSlot3[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[playSlot3[0]][3], (playSlot3[1], playerCardY, cardWidth, cardHeight))
			messagetoscreen(str(playSlot3[3]), x=playSlot3[1], y=playSlot3[2] + cardHeight/2)
			messagetoscreen(str(playSlot3[4]), x=playSlot3[1] + cardWidth - handSpacing, y=playSlot3[2] + cardHeight/2)
		if playSlot4[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[playSlot4[0]][3], (playSlot4[1], playerCardY, cardWidth, cardHeight))
			messagetoscreen(str(playSlot4[3]), x=playSlot4[1], y=playSlot4[2] + cardHeight/2)
			messagetoscreen(str(playSlot4[4]), x=playSlot4[1] + cardWidth - handSpacing, y=playSlot4[2] + cardHeight/2)
		if playSlot5[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[playSlot5[0]][3], (playSlot5[1], playerCardY, cardWidth, cardHeight))
			messagetoscreen(str(playSlot5[3]), x=playSlot5[1], y=playSlot5[2] + cardHeight/2)
			messagetoscreen(str(playSlot5[4]), x=playSlot5[1] + cardWidth - handSpacing, y=playSlot5[2] + cardHeight/2)

		if opponentSlot1[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[opponentSlot1[0]][3], (opponentSlot1[1], opponentCardY, cardWidth, cardHeight))
			messagetoscreen(str(opponentSlot1[3]), x=opponentSlot1[1], y=opponentSlot1[2] + cardHeight/2)
			messagetoscreen(str(opponentSlot1[4]), x=opponentSlot1[1] + cardWidth - handSpacing, y=opponentSlot1[2] + cardHeight/2)
		if opponentSlot2[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[opponentSlot2[0]][3], (opponentSlot2[1], opponentCardY, cardWidth, cardHeight))
			messagetoscreen(str(opponentSlot2[3]), x=opponentSlot2[1], y=opponentSlot2[2] + cardHeight/2)
			messagetoscreen(str(opponentSlot2[4]), x=opponentSlot2[1] + cardWidth - handSpacing, y=opponentSlot2[2] + cardHeight/2)
		if opponentSlot3[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[opponentSlot3[0]][3], (opponentSlot3[1], opponentCardY, cardWidth, cardHeight))
			messagetoscreen(str(opponentSlot3[3]), x=opponentSlot3[1], y=opponentSlot3[2] + cardHeight/2)
			messagetoscreen(str(opponentSlot3[4]), x=opponentSlot3[1] + cardWidth - handSpacing, y=opponentSlot3[2] + cardHeight/2)
		if opponentSlot4[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[opponentSlot4[0]][3], (opponentSlot4[1], opponentCardY, cardWidth, cardHeight))
			messagetoscreen(str(opponentSlot4[3]), x=opponentSlot4[1], y=opponentSlot4[2] + cardHeight/2)
			messagetoscreen(str(opponentSlot4[4]), x=opponentSlot4[1] + cardWidth - handSpacing, y=opponentSlot4[2] + cardHeight/2)
		if opponentSlot5[0] != cardIDs[0]:
			pygame.draw.rect(gameDisplay, cards[opponentSlot5[0]][3], (opponentSlot5[1], opponentCardY, cardWidth, cardHeight))
			messagetoscreen(str(opponentSlot5[3]), x=opponentSlot5[1], y=opponentSlot5[2] + cardHeight/2)
			messagetoscreen(str(opponentSlot5[4]), x=opponentSlot5[1] + cardWidth - handSpacing, y=opponentSlot5[2] + cardHeight/2)

		if fullHandMessageTime > 0:
			messagetoscreen("Discard or play card before drawing another")
			fullHandMessageTime -= 1
		
		pygame.display.update()
		clock.tick(FPS)

gameloop()

pygame.quit()
quit()

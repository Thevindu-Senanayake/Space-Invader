import pygame
import random

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("Space Invaders")

# Set icon
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("ufo.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

movement_speed = 1

# Loop until the user clicks the close button.
done = False
while done == False:

	# Set the screen background and update the screen
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		# If keystroke is pressed check whether right or left
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -movement_speed
			if event.key == pygame.K_RIGHT:
				playerX_change = movement_speed
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	#  All drawing code happens after the for loop and but
	#  inside the main while done == False loop.

	playerX += playerX_change

	# set boundaries for player
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()

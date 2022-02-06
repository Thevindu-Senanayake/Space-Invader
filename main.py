from turtle import speed
import pygame

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

def player(x, y):
	screen.blit(playerImg, (x, y))

movement_speed = 0.3

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
	player(playerX, playerY)
	pygame.display.update()

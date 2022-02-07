import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

# Background Image
background_image = pygame.image.load("background.png")

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
enemyX_change = 4
enemyY_change = 10

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_state = "ready"

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x + 16, y + 10))

def fire_enemy(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
	if distance < 27:
		return True
	else:
		return False

movement_speed = 5
score = 0

# Loop until the user clicks the close button.
done = False
while done == False:

	# Set the screen background and update the screen
	screen.fill((0, 0, 0))

	# Set background color
	screen.blit(background_image, [0, 0])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		# If keystroke is pressed check whether right or left
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -movement_speed
			if event.key == pygame.K_RIGHT:
				playerX_change = movement_speed
			if event.key == pygame.K_SPACE and bullet_state is "ready":
				# Get the current x coordinate of the spaceship
				bulletX = playerX
				fire_bullet(bulletX, bulletY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	#  All drawing code happens after the for loop and but
	#  inside the main while done == False loop.

	#  Move the player
	playerX += playerX_change

	# set boundaries for player
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	# Move the enemy
	enemyX += enemyX_change

	# set boundaries for enemy
	if enemyX <= 0:
		enemyX_change = 4
		enemyY += enemyY_change
	elif enemyX >= 736:
		enemyX_change = -4
		enemyY += enemyY_change

	# Reset the bullet state and x, y coordinates
	if bulletY <= 0:
		bulletY = 480
		bullet_state = "ready"

	# Move the bullet
	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	# Check for bullet collision with enemy
	isFired = fire_enemy(enemyX, enemyY, bulletX, bulletY)
	if isFired:
		bulletY = 480
		bullet_state = "ready"
		score += 1
		print("Score: " + str(score))
		enemyX = random.randint(0, 735)
		enemyY = random.randint(50, 150)

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()

import pygame
from random import randint

pygame.init()
pygame.display.set_caption('Flappy Bird')
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def write_text_on_screen(font, text, x_pos, y_pos):
	text = font.render(text, True, (0,0,0))
	screen.blit(text, (x_pos, y_pos))

def main():
	running = True
	GREEN = (0,255,0)
	RED = (255,0,0)
	BLUE = (0,0,255)
	YELLOW = (255,255,0)
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	GRAVITY = 0.5
	clock = pygame.time.Clock()
	TUBE_WIDTH = 50
	TUBE_VELOCITY = 3
	TWO_TUBE_DISTANCE_HOR = 300
	TWO_TUBE_DISTANCE_VER = 200
	TUBE_HEIGHT_MIN, TUBE_HEIGHT_MAX = 80, 300
	BIRD_WIDTH, BIRD_HEIGHT = 40, 40
	tube1_x = SCREEN_WIDTH*1.5
	tube1_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
	tube2_x = tube1_x + randint(200,TWO_TUBE_DISTANCE_HOR)
	tube2_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
	tube3_x = tube2_x + randint(200,TWO_TUBE_DISTANCE_HOR)
	tube3_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
	tube_y = 0
	font = pygame.font.SysFont("sans", 30)
	bird_x = 10
	bird_y = 300
	bird_velocity = 0
	score = 0
	is_tube_passed = False
	is_game_over = False

	background_image = pygame.image.load("background.png")
	bird_image = pygame.image.load("bird.png")
	bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

	while running:
		clock.tick(60)
		screen.fill(GREEN)
		screen.blit(background_image, (0,0))

		tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, tube_y, TUBE_WIDTH, tube1_height))
		tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TWO_TUBE_DISTANCE_VER, TUBE_WIDTH, SCREEN_HEIGHT - tube1_height - TWO_TUBE_DISTANCE_VER))

		tube2_rect = pygame.draw.rect(screen, RED, (tube2_x, tube_y, TUBE_WIDTH, tube2_height))
		tube2_rect_inv = pygame.draw.rect(screen, RED, (tube2_x, tube2_height + TWO_TUBE_DISTANCE_VER, TUBE_WIDTH, SCREEN_HEIGHT - tube2_height - TWO_TUBE_DISTANCE_VER))

		tube3_rect = pygame.draw.rect(screen, YELLOW, (tube3_x, tube_y, TUBE_WIDTH, tube3_height))
		tube3_rect_inv = pygame.draw.rect(screen, YELLOW, (tube3_x, tube3_height + TWO_TUBE_DISTANCE_VER, TUBE_WIDTH, SCREEN_HEIGHT - tube3_height - TWO_TUBE_DISTANCE_VER))

		tube1_x -= TUBE_VELOCITY
		tube2_x -= TUBE_VELOCITY
		tube3_x -= TUBE_VELOCITY

		bird_rect = screen.blit(bird_image, (bird_x, bird_y))
		bird_y += bird_velocity
		bird_velocity += GRAVITY

		sand_rect = pygame.draw.rect(screen, YELLOW, (0, 550, SCREEN_WIDTH, SCREEN_HEIGHT - 500))

		write_text_on_screen(font, "Score: " + str(score), 5, 5)

		if (bird_x > (tube1_x + TUBE_WIDTH)) and is_tube_passed == False:
			score += 1
			is_tube_passed = True

		if (bird_x > (tube2_x + TUBE_WIDTH)) and is_tube_passed == False:
			score += 1
			is_tube_passed = True

		if (bird_x > (tube3_x + TUBE_WIDTH)) and is_tube_passed == False:
			score += 1
			is_tube_passed = True

		for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect]:
			if bird_rect.colliderect(tube):
				is_game_over = True
				TUBE_VELOCITY = 0
				bird_velocity = 0
				write_text_on_screen(font, "Game Over, Score: " + str(score), 80, 200)
				write_text_on_screen(font, "Press Space to play again", 50, 240)

		if tube1_x < -TUBE_WIDTH:
			tube1_x = SCREEN_WIDTH
			tube1_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
			is_tube_passed = False
			while (abs(tube2_x - tube1_x) < TUBE_WIDTH*4) or (abs(tube3_x - tube1_x) < TUBE_WIDTH*4):
				tube1_x = SCREEN_WIDTH + randint(0,TWO_TUBE_DISTANCE_HOR)

		if tube2_x < -TUBE_WIDTH:
			tube2_x = SCREEN_WIDTH + randint(0,TWO_TUBE_DISTANCE_HOR)
			tube2_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
			is_tube_passed = False
			while (abs(tube2_x - tube1_x) < TUBE_WIDTH*4) or (abs(tube3_x - tube2_x) < TUBE_WIDTH*4):
				tube2_x = SCREEN_WIDTH + randint(0,TWO_TUBE_DISTANCE_HOR)
			
		if tube3_x < -TUBE_WIDTH:
			tube3_x = SCREEN_WIDTH + randint(0,TWO_TUBE_DISTANCE_HOR)
			tube3_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
			is_tube_passed = False
			while (abs(tube3_x - tube2_x) < TUBE_WIDTH*4) or (abs(tube3_x - tube1_x) < TUBE_WIDTH*4):
				tube3_x = SCREEN_WIDTH + randint(0,TWO_TUBE_DISTANCE_HOR)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if is_game_over:
						bird_x, bird_y = 10, 300
						bird_velocity = 0
						tube1_x = SCREEN_WIDTH*1.5
						tube1_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
						tube2_x = tube1_x + randint(200,TWO_TUBE_DISTANCE_HOR)
						tube2_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
						tube3_x = tube2_x + randint(200,TWO_TUBE_DISTANCE_HOR)
						tube3_height = randint(TUBE_HEIGHT_MIN,TUBE_HEIGHT_MAX)
						TUBE_VELOCITY = 3
						score = 0
						is_game_over = False
					else:
						bird_velocity = 0
						bird_velocity -= 10
			if event.type == pygame.QUIT:
				running = False
					
		pygame.display.flip()

	pygame.quit()

main()
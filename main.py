import pygame
import time
import random
pygame.font.init()

#AUTOMATIC DOWNLOAD FOR PIP PACKAGE LIBRARY NEED TO IMPLELEMT: this will check someones elses computer if they are trying to play the game and run pip
#automatically if they have it if not it will automatically download what they need in their computer to play the game

#you need more open source contributions 


# creating the pygame window
WIDTH, HEIGHT = 1000, 800  # IN PIXELS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("falling tears")

# Load background and player images
BG = pygame.image.load("corrupted_clouds.jpg")
PLAYER_IMAGE = pygame.image.load("Carolina.png")

# main game logic
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100
PLAYER_VEL = 5

FONT = pygame.font.SysFont("courtier", 30)
def draw(player_rect, elapsed_time):
    WIN.blit(BG, (0, 0))
    WIN.blit(PLAYER_IMAGE, player_rect.topleft)
    
    time_text = FONT.render(f"TIME: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))
    pygame.display.update()


def main():
    run = True
    player_rect = pygame.Rect((WIDTH - 500) // 2, HEIGHT - 400, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    start_time = time.time()
    elapsed_time = 0 

    star_add_increment = 2000

    star_count = 0 

    stars = []



    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time 

        if star_count > star_add_increment:
            for _ in range(3):
                start_x = random.ranint(0, WIDTH - STARWID)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_rect.x - PLAYER_VEL >= 0: #K_X gives you whatever key you want 
            player_rect.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player_rect.x + PLAYER_VEL + player_rect.width <= WIDTH: #K_X gives you whatever key you want 
            player_rect.x += PLAYER_VEL
         




        draw(player_rect, elapsed_time)

        clock.tick(60)  # Set the frame rate to 60 frames per second

    pygame.quit()


# save an image and put it in the same dir as your python script

#if __name__ == "__main__":
 #   main()

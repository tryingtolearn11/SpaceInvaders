import pygame
pygame.init()

# BACKGROUND
bg = pygame.image.load('space.jpg')

# Player model
char = pygame.image.load('bgbattleship.png')


def main():
    global fps, fpsClock
    fps = 40
    screenWidth = 500
    screenHeight = 600
    displayWindow = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("SPACE BATTLE")
    fpsClock = pygame.time.Clock()
    x = 50
    y = 50
    width = 40
    height = 60
    speed = 29

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_a] and x > speed:
                x -= speed

            if keys[pygame.K_d] and x < screenWidth - width - speed:
                x += speed

            if keys[pygame.K_w] and y > speed:
                y -= speed

            if keys[pygame.K_s] and y < screenHeight - height - speed:
                y += speed

        displayWindow.blit(bg, (0, 0))
        displayWindow.blit(char, (x, y))
        pygame.display.update()
        fpsClock.tick(fps)


main()

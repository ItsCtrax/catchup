import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Cath")

IMAGE = pygame.image.load("sprite1.png").convert_alpha()
IMAGE = pygame.transform.scale(IMAGE, (50, 50))

sprite2 = pygame.image.load("sprite2.png").convert_alpha()
sprite2 = pygame.transform.scale(sprite2, (50, 50))

background = pygame.transform.scale(pygame.image.load("background.png"), (700, 500))

rect = IMAGE.get_rect()
rect.center = (10, 10)

rect2 = sprite2.get_rect()
rect2.center = (100, 100)

clock = pygame.time.Clock()
desired_fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # Boundary checks for sprite1
    if keys[pygame.K_LEFT]:
        if rect.left > 0:
            rect.move_ip(-2, 0)
    if keys[pygame.K_RIGHT]:
        if rect.right < 700:
            rect.move_ip(2, 0)
    if keys[pygame.K_UP]:
        if rect.top > 0:
            rect.move_ip(0, -2)
    if keys[pygame.K_DOWN]:
        if rect.bottom < 500:
            rect.move_ip(0, 2)

    # Boundary checks for sprite2
    if keys[pygame.K_a]:
        if rect2.left > 0:
            rect2.move_ip(-2, 0)
    if keys[pygame.K_d]:
        if rect2.right < 700:
            rect2.move_ip(2, 0)
    if keys[pygame.K_w]:
        if rect2.top > 0:
            rect2.move_ip(0, -2)
    if keys[pygame.K_s]:
        if rect2.bottom < 500:
            rect2.move_ip(0, 2)

    window.blit(background, (0, 0))
    window.blit(IMAGE, rect)
    window.blit(sprite2, rect2)
    pygame.display.update()

    clock.tick(desired_fps)

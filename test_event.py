import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        print('Quit')

    if event.type == pygame.KEYDOWN:
        print('Key Down')
        print(event.key)
        print(event.unicode)

    if event.type == pygame.KEYUP:
        print('Key Up')
        print(event.key)

    if event.type == pygame.MOUSEBUTTONDOWN:
        print('Mouse Button Down')
        print(event.pos)
        print(event.button == pygame.BUTTON_RIGHT)
        print(event.button == pygame.BUTTON_LEFT)

    if event.type == pygame.MOUSEBUTTONUP:
        print('Mouse Button Up')
        print(event.pos)
        print(event.button == pygame.BUTTON_RIGHT)
        print(event.button == pygame.BUTTON_LEFT)

    if event.type == pygame.MOUSEMOTION:
        print('Mouse Motion')
        print(event.pos)
        print(event.rel)



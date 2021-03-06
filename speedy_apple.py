import pygame

pygame.init()

window_surface = pygame.display.set_mode((400, 400))

class Apple(pygame.sprite.Sprite):

    def __init__(self, image, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

apple_image = pygame.image.load('./images/apple.png')
my_apple = Apple(apple_image, 100, 100)

apple_group = pygame.sprite.Group()
apple_group.add(my_apple)

game_ended = False
while not game_ended:
    for event in pygame.event.get():
        pass

    window_surface.fill((0, 0, 0))
    apple_group.draw(window_surface)

    pygame.display.update()

pygame.quit()

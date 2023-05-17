import pygame

home_image           = r"../image/home.png"
home_destroyed_image = r"../image/home_destroyed.png"

class Create_Home(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(home_destroyed_image)
        self.rect = self.image.get_rect()

class Home():
    def __init__(self):
        self.homeGroup = pygame.sprite.Group()
        self.homeDefault = Create_Home()
        self.homeDefault.rect.left = 3 + 12 * 24
        self.homeDefault.rect.top = 3 + 24 * 24
        self.homeGroup.add(self.homeDefault)

import pygame


class Blackship(pygame.sprite.Sprite):
    on_screen = False

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        Blackship.on_screen = True

    def follow(self, sprite):
        if self.rect.x < sprite.rect.x:
            self.rect.x += 2
        elif self.rect.x > sprite.rect.x:
            self.rect.x -= 2
        if self.rect.y < sprite.rect.y:
            self.rect.y += 2
        elif self.rect.y > sprite.rect.y:
            self.rect.y -= 2

# TODO: make the blackship change the on_screen variable to false upon death

import pygame
import random


pygame.init()


SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2



BLUE = pygame.Colour('Blue')
LIGHTBLUE = pygame.Colour('Lightblue')
DARKBLUE = pygame.Colour('Darkblue')


YELLOW = pygame.Colour('Yellow')
MAGENTA = pygame.colour('Magenta')
ORANGE = pygame.Colour('Orange')
WHITE = pygame.Colour('White')



class Sprite(pygame.sprite.Sprite):


    def __init__(self, colour, height, width):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.velocity[random.choice([-1, 1]), random.choice([-1, 1])]


        def update(self):

            self.rect.move_ip(self.velocity)

            boundary_hit = False

            if self.rect.left <= 0 or self.rect.right >= 500:
                self.velocity[0] = -self.velocity[0]
                boundary_hit = True

                if self.rect.top <= 0 or self.rect.bottom >= 400:
                    self.velocity[1] = -self.velocity[1]
                    boundary_hit = True


                    if boundary_hit:
                        pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
                        pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))


    def change_colour(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))



def change_background_colour():
    global bg_ colour
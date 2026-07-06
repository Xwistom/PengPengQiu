import pygame

class Logo:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/logo.bmp")
        self.rect = self.image.get_rect()
        self.rect.x=325
        self.rect.y=50

    def blitme(self):
        self.screen.blit(self.image,self.rect)

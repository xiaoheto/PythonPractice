import sys
import pygame
from settings import Settings
from figure import Figure

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.figure = Figure(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # allow the figure to move
                if event.key == pygame.K_RIGHT:
                    self.figure.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.figure.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.figure.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.figure.moving_left = False

    def _updrade_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.figure.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            # listen to the events from the keyboard and the mouse
            self._check_events()

            self.figure.update()

            self._updrade_screen()

            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
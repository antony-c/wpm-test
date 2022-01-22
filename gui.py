import pygame
from colours import Colours

class GUI:

    def __init__(self, word_manager):
        self.screen = pygame.display.set_mode([1000, 800])
        self.font = pygame.font.Font(None, 52)

        self.word_manager = word_manager

    def update(self, user_input, elapsed, words, accuracy, wpm):
        self.screen.fill(Colours.BLACK)

        self.draw_text_box(user_input, 0, 400)
        self.draw_text_box(f"{words}", 0, 300)
        self.draw_text_box(f"{int(elapsed)}s elapsed!", 0, 210)
        self.draw_text_box(f"{wpm} WPM.", 100, 210)
        self.draw_text_box(f"{accuracy}", 700, 210)

        pygame.display.flip()

    def draw_main_screen(self):
        self.screen.fill(Colours.BLACK)
        self.draw_text_box(f"{self.word_manager.get_accuracy()}% accuracy!", 300)
        pygame.display.flip()

    def draw_text_box(self, text, x, y):
        text_surface = self.font.render(text, True, Colours.WHITE)

        width = text_surface.get_width()
        height = text_surface.get_height()

        center = 500 - width // 2

        # If x argument is 0, x is center
        if not x:
            x = center

        background = pygame.Rect(x - 6, y - 6, width + 13, height + 13)

        pygame.draw.rect(self.screen, Colours.MID_GREEN, background, 0, 20)
        self.screen.blit(text_surface, [x, y])

import pygame

class Input_Manager:

    def __init__(self, word_manager):
        self.user_input = str()
        self.word_manager = word_manager

    def update(self, text):
        if text.key == pygame.K_BACKSPACE:
            self.user_input = self.user_input[0:-1]
        elif text.key == pygame.K_SPACE or text.key == pygame.K_RETURN:
            self.word_manager.next(self.user_input)
            self.user_input = str()
        else:
            self.user_input += text.unicode

import pygame, sys, time
from input_manager import Input_Manager
from gui import GUI
from word_manager import Word_Manager

pygame.init()

def run_game():
    def get_elapsed():
        return time.time() - start_time

    def get_words():
        current_word = word_manager.current_word
        index = word_manager.index
        list_words = [word_manager.words[index + i] for i in range(1, 5)]
        words = f"{current_word} {' '.join(word for word in list_words)}"

        return words

    def get_wpm():
        wpm = int()
        if elapsed:
            wpm = round(word_manager.correct_count / elapsed * 60)
        return wpm

    def get_accuracy():
        return f"{word_manager.get_accuracy()}% accuracy!"

    clock = pygame.time.Clock()
    start_time = time.time()

    word_manager = Word_Manager()
    input_manager = Input_Manager(word_manager)
    gui = GUI(word_manager)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                input_manager.update(event)

        elapsed = get_elapsed()
        words = get_words()
        wpm = get_wpm()
        accuracy = get_accuracy()

        # If 1 minute passed, return stats for end screen. Else, continue
        if int(elapsed) == 60:
            return (wpm, accuracy)
        else:
            gui.update(input_manager.user_input, elapsed, words, accuracy, wpm)

        clock.tick(60)

while True:
    run_game()

import pygame
from random import sample

class Word_Manager:

    def __init__(self):
        self.words = self.get_words()
        self.index = 0
        self.current_word = self.words[self.index]

        self.correct_count = 0
        self.typed_count = 0

    def next(self, user_input):
        if user_input == self.current_word:
            self.correct_count += 1
        self.typed_count += 1

        self.index += 1
        self.current_word = self.words[self.index]

    def get_accuracy(self):
        accuracy = 100
        if self.typed_count > 0:
            accuracy = round(self.correct_count / self.typed_count * 100, 2)
        return accuracy

    def get_words(self):
        words = """always then of letter black sometimes take man by too see
        small first will children water always fire here fall through hand were
        last still study back year every too might thing new set get change
        people each her our you boy answer have of was at another at our other
        same year red almost saw or does would until another own tree should
        over seem song red man do let long walk each year end those put really
        man paper food read plant spell line really out always study house
        father best song they then last later because house are his hand
        city man earth few when start three last four own air from got idea
        just food they let few place did day over they book where we in
        found will animal day use than around often sea its us there food
        once spell father black men how because river must my answer form
        think ask light run paper home try back enough on up were want would
        did need right play carry that animal fire new letter most begin three
        some grow day very work carry first out all right live does one in then
        their to along tree be said sea after talk state miss later run down
        some being point night tell carry light enough sea away does near big
        move must ask left all car away their what hear long very seem then
        small at always sometimes right men really oil then here day be came
        your here him until say point still away change big far some along
        there soon word was"""
        words = words.split()
        words = sample(words, len(words))
        return words

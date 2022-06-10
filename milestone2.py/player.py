from card import values, ranks, suits,Card
from deck import Deck

class player:

    def __init__ (self, name):
        self. name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards):
        pass
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)}.'



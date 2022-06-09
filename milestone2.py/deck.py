from card import values, ranks, suits,Card
import random


class Deck:

    def __init__(self):
        self.all_cards= []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        
 

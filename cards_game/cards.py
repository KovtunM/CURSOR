import itertools
import random
from enum import Enum

_ranks = [6, 7, 8, 9, 10,
          'J', 'Q', 'K', 'A']
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}


class SuitEnum(Enum):
    def __str__(cls):
        return cls.value


Suit = SuitEnum('Suit', _suits)


class Card:
    __slots__ = 'rank', 'suit'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class CardDeckBase:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank, suit in itertools.product(_ranks, _suits)]

    def deal(self, n=1):
        return [self.cards.pop() for _ in range(n)]


class FrenchDeck(CardDeckBase):
    pass


if __name__ == '__main__':
    deck = FrenchDeck()
    while True:
        try:
            num_cards = int(input('\nHow many cards to deal? (Enter 0 to quit): '))
            if num_cards == 0:
                print('\nGoodbye.')
                break
            elif num_cards < 0 or num_cards > len(deck.cards):
                print(f'\nInvalid number of cards. Deck has {len(deck.cards)} cards.')
                continue
            random.shuffle(deck.cards)
            dealt_cards = deck.deal(num_cards)
            for card in dealt_cards:
                print(f'{card.rank} of {card.suit}')
        except ValueError:
            print('\nInvalid input. Please enter a number.')

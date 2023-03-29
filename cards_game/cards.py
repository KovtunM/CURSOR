import itertools
import random
from enum import Enum


class SuitEnum(Enum):
    SPADES = '\u2660'
    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'

    def __str__(self):
        return self.value


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class CardDeck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank, 
        suit in itertools.product(range(2, 15), SuitEnum)]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __add__(self, other):
        if isinstance(other, Card):
            self.cards.append(other)
        elif isinstance(other, CardDeck):
            self.cards.extend(other.cards)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, card):
        if isinstance(card, Card):
            self.cards.remove(card)
        elif isinstance(card, tuple) and len(card) == 2:
            self.cards = [c for c in self.cards if (c.rank, c.suit) != card]
        else:
            raise TypeError("Unsupported operand type for -")

    def __contains__(self, card):
        if isinstance(card, Card):
            return card in self.cards
        elif isinstance(card, tuple) and len(card) == 2:
            return any(c.rank == card[0] and c.suit == card[1] for c in self.cards)
        else:
            raise TypeError("Unsupported operand type for 'in'")

    def __eq__(self, other):
        if isinstance(other, CardDeck):
            return set(self.cards) == set(other.cards)
        else:
            return False


class SmallDeck(CardDeck):
    def __init__(self):
        self.cards = [Card(rank, suit) for rank, 
        suit in itertools.product(range(7, 15), SuitEnum)]


class ClassicDeck(CardDeck):
    pass


if __name__ == '__main__':
    deck = ClassicDeck()
    print("Initial deck:")
    for card in deck:
        print(card)

    deck.shuffle()
    print("\nShuffled deck:")
    for card in deck:
        print(card)

    print(f"\nNumber of cards in deck: {len(deck)}")

    card1 = deck[0]
    card2 = deck[1]
    print(f"\nDrawing card: {card1}")
    deck - card1
    print(f"Number of cards in deck: {len(deck)}")

    print(f"\nPutting card {card1} back in the deck")
    deck + card1
    print(f"Number of cards in deck: {len(deck)}")

    print(f"\nChecking if {card2} is in the deck: {card2 in deck}")
    print(f"Checking if Ace of Spades is in the deck: {('A', SuitEnum.SPADES) in deck}")

    deck2 = ClassicDeck()
    deck3 = SmallDeck()
    print(f"\nChecking if two identical decks are equal: {deck == deck2}")
    print(f"Checking if two different decks are equal: {deck == deck3}")


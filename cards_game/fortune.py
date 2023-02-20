import random
from cards import FrenchDeck


def _get_card_meaning(card):
    meanings = {
        'A': 'You will experience a major life change.',
        'K': 'You will face a challenge that you must overcome.',
        'Q': 'You will make a new friend or find new love.',
        'J': 'You will receive unexpected news.',
        '10': 'You will embark on a new adventure.',
        '9': 'You will find happiness and contentment.',
        '8': 'You will face a disappointment or setback.',
        '7': 'You will receive good news or a positive outcome.',
        '6': 'You will encounter a difficult decision or choice.'
    }
    return meanings.get(card.rank, 'Unknown meaning.')


class FortuneTeller:
    def __init__(self, deck):
        self.deck = deck

    def _draw_card(self):
        return self.deck.deal(1)[0]

    def tell_fortune(self):
        random.shuffle(self.deck.cards)
        card = self._draw_card()
        print(f'\nYou drew the {card.rank} of {card.suit}.')
        meaning = _get_card_meaning(card)
        print(f'The meaning of this card is: {meaning}')


if __name__ == '__main__':
    deck = FrenchDeck()
    fortune_teller = FortuneTeller(deck)
    while True:
        try:
            run = input('\nPress enter to receive your fortune (or enter "q" to exit): ')
            fortune_teller.tell_fortune()
            if run == 'q':
                print('\nGoodbye.')
                break
        except (KeyboardInterrupt, EOFError):
            break

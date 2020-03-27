
from functools import total_ordering
from random import shuffle, sample


@total_ordering
class Card(object):
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    SUIT_EMOJIS = ("♣", "♦", "♥", "♠")
    NUMBERS = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, suit, number):
        # Normalize inputs
        suit = suit.title()
        number = str(number)

        # Check for valid input
        if not (suit in self.SUITS and number in self.NUMBERS):
            raise ValueError("Invalid card")

        # Enconde as indexes
        self._suit = self.SUITS.index(suit)
        self._number = self.NUMBERS.index(number)

    @property
    def suit(self):
        return self.SUITS[self._suit]

    @property
    def number(self):
        return self.NUMBERS[self._number]

    def __repr__(self):
        return f"Card(suit='{self.suit}', number='{self.number}')"

    def __str__(self):
        return f"{self.number}{self.SUIT_EMOJIS[self._suit]}"

    def __eq__(self, other):
        return (self._suit == other._suit and
                self._number == other._number)

    def __gt__(self, other):
        if self._suit == other._suit:
            return self._number > other._number
        else:
            return self._suit > other._suit


class CardDeck(object):
    def __init__(self):
        self._cards = [Card(suit, number)
                       for suit in Card.SUITS for number in Card.NUMBERS]

    def shuffle(self):
        shuffle(self._cards)

    def pull_random_cards(self, amount):
        return sample(self._cards, amount)

    def __str__(self):
        return "\n".join(str(card) for card in self._cards)


ENCODING = {
    (0, 1, 2): 1,
    (0, 2, 1): 2,
    (1, 0, 2): 3,
    (1, 2, 0): 4,
    (2, 0, 1): 5,
    (2, 1, 0): 6,
}


def guess_hidden_card(shown_cards):
    # Fist card dictates the suit
    fist_card = shown_cards[0]
    suit = fist_card.suit

    # Last three cards encode the number
    encoded_cards = shown_cards[1:]
    decoded = ENCODING[tuple(encoded_cards.index(card)
                             for card in sorted(encoded_cards))]

    number = Card.NUMBERS[(fist_card._number + decoded) % 13]

    return Card(suit, number)


test_cards = [
    Card('clubs', 7),
    Card('hearts', 'J'),
    Card('hearts', 7),
    Card('spades', 'Q'),
]

guessed = guess_hidden_card(test_cards)
print(guessed)
assert guessed == Card('Clubs', 10)

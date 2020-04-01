from functools import total_ordering
import random
import pytest

from common import most_frequent, indexes_if_sorted, sort_by_index


@total_ordering
class Card(object):
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    NUMBERS = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')
    __slots__ = ('_suit', '_number')

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

    @classmethod
    def from_str(cls, card):
        number, suit_initial = card.split('_')
        suit = [suit for suit in cls.SUITS if suit[0]
                == suit_initial.upper()][0]
        return cls(suit, number)

    @property
    def suit(self):
        return self.SUITS[self._suit]

    @property
    def number(self):
        return self.NUMBERS[self._number]

    def __repr__(self):
        return f"Card(suit='{self.suit}', number='{self.number}')"

    def __str__(self):
        return f"{self.number}_{self.SUITS[self._suit][0]}"

    def __hash__(self):
        return hash((self._suit, self._number))

    def __eq__(self, other):
        return (self._suit == other._suit and
                self._number == other._number)

    def __gt__(self, other):
        if self._suit == other._suit:
            return self._number > other._number
        else:
            return self._suit > other._suit


class CardDeck(list):
    def __init__(self, cards):
        super().__init__(cards)

    @classmethod
    def full(cls):
        return cls(Card(suit, number)
                   for suit in Card.SUITS
                   for number in Card.NUMBERS)

    def pull_random_cards(self, amount):
        return random.sample(self, amount)

    # def __str__(self):
    #     return "\n".join(str(card) for card in self._cards)


class Magic(object):
    ENCODING = {
        (0, 1, 2): 1,
        (0, 2, 1): 2,
        (1, 0, 2): 3,
        (1, 2, 0): 4,
        (2, 0, 1): 5,
        (2, 1, 0): 6,
    }

    @classmethod
    def encode(cls, number):
        for key, value in cls.ENCODING.items():
            if value == number:
                return key

    @classmethod
    def decode(cls, indexes):
        return cls.ENCODING[indexes]


class Magician(Magic):
    @classmethod
    def guess_hidden_card(cls, shown_cards):
        # Fist card dictates the suit
        fist_card = shown_cards[0]
        suit = fist_card.suit

        # Last three cards encode the number
        encoded_cards = shown_cards[1:4]
        indexes = indexes_if_sorted(encoded_cards)
        distance = cls.decode(indexes)

        number = Card.NUMBERS[(fist_card._number + distance) % 13]

        return Card(suit, number)


class Assistant(Magic):
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError("Exactly 5 cards are needed!")
        self.cards = tuple(cards)
        self._arranged = False

    @classmethod
    def from_random_cards(cls):
        cards = CardDeck.full().pull_random_cards(5)
        return cls(cards)

    @classmethod
    def from_input(cls):
        raise NotImplementedError

    def arrange_cards(self) -> None:
        # Select 2 cards with common suit
        suit = most_frequent(card.suit for card in self.cards)
        candidates = [card for card in self.cards
                      if card.suit == suit]
        small_card, big_card = sorted(candidates[:2])

        distance = big_card._number - small_card._number
        # Assert clockwise counting (Q, K, A, 2, 3...)
        if distance <= 6:
            guess_card = big_card
            first_card = small_card
        else:
            distance = 13-distance
            guess_card = small_card
            first_card = big_card

        arranged = [first_card]

        cards_to_code = [card for card in self.cards
                         if card not in {guess_card, first_card}]
        indexes = self.encode(distance)
        encoded_cards = sort_by_index(cards_to_code, indexes)

        arranged.extend(encoded_cards)
        arranged.append(guess_card)

        self.cards = tuple(arranged)
        self._arranged = True

    @property
    def card_to_guess(self):
        """That is, last card in arranged deck."""
        if not self._arranged:
            self.arrange_cards()
        return self.cards[-1]

    @property
    def cards_to_show(self):
        """First 4 cards in deck, properly arranged."""
        if not self._arranged:
            self.arrange_cards()
        return tuple(self.cards[:4])


test_cards = [
    Card('clubs', 7),
    Card('hearts', 'J'),
    Card('hearts', 7),
    Card('spades', 'Q'),
]
test_guessed = Card('Clubs', 10)

guessed = Magician.guess_hidden_card(test_cards)
print(guessed)
assert guessed == test_guessed


five_cards = test_cards + [test_guessed]


@pytest.mark.parametrize("seed", range(20))
def test_trick(seed):
    # Test trick with different random cards
    random.seed(seed)
    magician = Magician()
    assistant = Assistant.from_random_cards()
    hidden_card = assistant.card_to_guess
    shown_cards = assistant.cards_to_show
    assert magician.guess_hidden_card(shown_cards) == hidden_card

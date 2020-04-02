from functools import total_ordering
import random
import pytest

from common import most_frequent, indexes_if_sorted, sort_by_index, int_to_bin, bin_to_int


@total_ordering
class Card(object):
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    EMOJIS = ('🃑', '🃁', '🂱', '🂡')
    NUMBERS = ('A', '2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'Q', 'K')
    __slots__ = ('_suit', '_number')

    def __init__(self, suit, number):
        hidden = ((suit is None or suit == '?') and
                  (number is None or number == '?'))
        if hidden:
            self._suit = None
            self._number = None
        else:
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

    @classmethod
    def hidden(cls):
        """
        >>> Card.hidden()
        Card(suit='?', number='?')
        """
        return cls(None, None)

    @property
    def is_hidden(self):
        return (self._number is None and
                self._suit is None)

    @property
    def suit(self):
        if self.is_hidden:
            return '?'
        else:
            return self.SUITS[self._suit]

    @property
    def number(self):
        if self.is_hidden:
            return '?'
        else:
            return self.NUMBERS[self._number]

    def __repr__(self):
        return f"Card(suit='{self.suit}', number='{self.number}')"

    def __str__(self):
        return f"{self.number}_{self.SUITS[self._suit][0]}"

    def __hash__(self):
        return hash((self._suit, self._number))

    def __eq__(self, other):
        return ((type(self) == type(other)) and
                (self._suit, self._number) == (other._suit, other._number))

    def __gt__(self, other):
        if self.is_hidden or other.is_hidden:
            return NotImplementedError("Hidden cards cannot be compared")

        if self._suit == other._suit:
            return self._number > other._number
        else:
            return self._suit > other._suit

    @property
    def emoji(self):
        """
        >>> Card('Diamonds', 'K').emoji
        '🃎'
        """
        if self.is_hidden:
            return '🂠'
        else:
            ace_emoji = self.EMOJIS[self._suit]
            ascii_number = ord(ace_emoji) + self._number
            if self._number >= 12:
                ascii_number += 1
            return chr(ascii_number)

    @property
    def is_red(self):
        self.suit in ('Diamonds', 'Hearts')

    @property
    def is_black(self):
        not self.is_red


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
    def encode_sorting(cls, number) -> tuple:
        for key, value in cls.ENCODING.items():
            if value == number:
                return key

    @classmethod
    def decode_sorting(cls, indexes) -> int:
        return cls.ENCODING[indexes]

    @classmethod
    def encode_binary(cls, number) -> str:
        return int_to_bin(number, bits=4)

    @classmethod
    def decode_binary(cls, binary) -> int:
        return bin_to_int(binary)


class Magician(Magic):
    @classmethod
    def guess_fifth_card(cls, shown_cards):
        # Fist card dictates the suit
        fist_card = shown_cards[0]
        suit = fist_card.suit

        # Last three cards encode the number
        encoded_cards = shown_cards[1:4]
        indexes = indexes_if_sorted(encoded_cards)
        distance = cls.decode_sorting(indexes)

        number = Card.NUMBERS[(fist_card._number + distance) % 13]

        return Card(suit, number)

    @classmethod
    def guess_fourth_card(cls, shown_cards):
        # First visible card is an anchor
        for card in shown_cards:
            if not card.is_hidden:
                anchor = card
                break

        binary_code = ''.join('1' if card.is_hidden else '0'
                              for card in shown_cards)
        distance = cls.decode_binary(binary_code)
        full_deck = CardDeck.full()
        anchor_index = full_deck.index(anchor)
        guess_index = (anchor_index + distance) % len(full_deck)
        guess_card = full_deck[guess_index]

        return guess_card


class Assistant(Magic):
    def __init__(self, cards):
        if len(cards) not in (4, 5):
            raise NotImplementedError(
                f"Trick with {len(cards)} cards not implemented.")
        self._cards = tuple(cards)
        self._arranged_cards = None

    @classmethod
    def from_random_cards(cls, amount):
        cards = CardDeck.full().pull_random_cards(amount)
        return cls(cards)

    @classmethod
    def from_input(cls):
        raise NotImplementedError

    def arrange_cards(self) -> None:
        if self.is_five_cards_trick:
            self.arrange_five_cards()
        elif self.is_four_cards_trick:
            self.arrange_four_cards()

    @property
    def is_five_cards_trick(self):
        return len(self._cards) == 5

    @property
    def is_four_cards_trick(self):
        return len(self._cards) == 4

    def arrange_five_cards(self) -> None:
        # Select 2 cards with common suit
        suit = most_frequent(card.suit for card in self._cards)
        candidates = [card for card in self._cards
                      if card.suit == suit]
        small_card, big_card = sorted(candidates[: 2])

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

        cards_to_code = [card for card in self._cards
                         if card not in {guess_card, first_card}]
        indexes = self.encode_sorting(distance)
        encoded_cards = sort_by_index(cards_to_code, indexes)

        arranged.extend(encoded_cards)
        arranged.append(guess_card)

        self._arranged_cards = {
            'show': tuple([first_card, *encoded_cards]),
            'guess': guess_card
        }

    def arrange_four_cards(self) -> None:
        """ Select two cards whose distance is minimum and encode distance in binary
        >>> cards = (Card('Diamonds', 'A'),
        ...          Card('Clubs', 2),
        ...          Card('Hearts', 'A'),
        ...          Card('Clubs', 'A'))
        >>> assistant = Assistant(cards)
        >>> assistant.card_to_guess
        Card(suit='Clubs', number='2')
        >>> assistant.cards_to_show         # doctest: +NORMALIZE_WHITESPACE
        (Card(suit='Clubs', number='A'), Card(suit='Hearts', number='A'), \
         Card(suit='Diamonds', number='A'), Card(suit='?', number='?'))
        """
        # Select cards based on relative distance
        cards = sorted(self._cards)
        full_deck = CardDeck.full()
        distances = []
        for i, card in enumerate(cards):
            previous_card = cards[i-1]
            distance = (full_deck.index(card) -
                        full_deck.index(previous_card)) % len(full_deck)
            distances.append(distance)

        distance = min(distances)
        min_distance_index = distances.index(distance)
        guess_card = cards[min_distance_index]
        anchor_card = cards[min_distance_index-1]
        rest_of_cards = [card for card in cards
                         if card not in (guess_card, anchor_card)]

        # Cards encoded in binary:
        # 0 = shown
        # 1 = hidden
        # First shown card is the anchor card, this is important for magician
        # First hidden card is the card to guess (this doesn't matter)
        encoded_cards = list(self.encode_binary(distance))
        first_shown = encoded_cards.index('0')
        encoded_cards[first_shown] = anchor_card
        for i, bit in enumerate(encoded_cards):
            if bit == '0':
                encoded_cards[i] = rest_of_cards.pop()
            elif bit == '1':
                encoded_cards[i] = Card.hidden()

        self._arranged_cards = {
            'show': tuple(encoded_cards),
            'guess': guess_card
        }

    @property
    def card_to_guess(self):
        if not self._arranged_cards:
            self.arrange_cards()
        return self._arranged_cards['guess']

    @property
    def cards_to_show(self):
        if not self._arranged_cards:
            self.arrange_cards()
        return self._arranged_cards['show']


def test_five_cards_trick():
    test_cards = [
        Card('clubs', 7),
        Card('hearts', 'J'),
        Card('hearts', 7),
        Card('spades', 'Q'),
    ]
    test_guessed = Card('Clubs', 10)

    guessed = Magician.guess_fifth_card(test_cards)
    assert guessed == test_guessed


@pytest.mark.parametrize("seed", range(20))
def test_five_cards_trick_random(seed):
    # Test trick with different random cards
    random.seed(seed)
    magician = Magician()
    assistant = Assistant.from_random_cards(5)
    assistant.arrange_cards()
    hidden_card = assistant.card_to_guess
    shown_cards = assistant.cards_to_show
    assert magician.guess_fifth_card(shown_cards) == hidden_card


@pytest.mark.parametrize("seed", range(20))
def test_four_cards_trick_random(seed):
    # Test trick with different random cards
    random.seed(seed)
    magician = Magician()
    assistant = Assistant.from_random_cards(4)
    assistant.arrange_cards()
    hidden_card = assistant.card_to_guess
    shown_cards = assistant.cards_to_show
    assert magician.guess_fourth_card(shown_cards) == hidden_card

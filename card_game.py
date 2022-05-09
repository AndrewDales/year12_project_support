from random import shuffle


class Card:
    suits = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}
    ranks = {"2": "Two",
             "3": "Three",
             "4": "Four",
             "5": "Five",
             "6": "Six",
             "7": "Seven",
             "8": "Eight",
             "9": "Nine",
             "10": "Ten",
             "J": "Jack",
             "Q": "Queen",
             "K": "King",
             "A": "Ace",
             }

    def __init__(self, rank, suit):

        if rank in self.ranks:
            self.rank = rank
        else:
            raise TypeError("Invalid rank")
        if suit.upper() in self.suits.keys():
            self.suit = suit.upper()
        else:
            raise TypeError("Invalid suit")

    @property
    def _rank_order(self):
        suit_list = list(self.suits)
        rank_list = list(self.ranks)
        return suit_list.index(self.suit), rank_list.index(self.rank)

    def __repr__(self):
        return f'Card <{self.rank[self.rank]} of {self.suits[self.suit]}>'

    def __eq__(self, other):
        return self._rank_order == other._rank_order

    def __lt__(self, other):
        return self._rank_order < other._rank_order


class CardSet:
    cards = []

    def __init__(self, card_list=None):
        if card_list:
            self.cards = [card for card in card_list]
        else:
            self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, card):
        try:
            self.cards.remove(card)
        except ValueError:
            print("Card not in list")
            raise
        else:
            return card

    def __repr__(self):
        return repr(self.cards)


class Deck(CardSet):

    def __init__(self):
        super().__init__()
        for suit in Card.suits:
            for rank in Card.ranks:
                self.add_card(Card(rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, num_players, num_cards):
        hands = [[self.play_card(card) for card in self.cards[:num_cards]] for _ in range(num_players)]
        return hands

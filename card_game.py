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
            raise ValueError("Invalid rank")
        if suit.upper() in self.suits.keys():
            self.suit = suit.upper()
        else:
            raise ValueError("Invalid suit")

    @property
    def rank_order(self):
        suit_list = list(self.suits)
        rank_list = list(self.ranks)
        return rank_list.index(self.rank), suit_list.index(self.suit)

    def __repr__(self):
        return f'Card <{self.ranks[self.rank]} of {self.suits[self.suit]}>'

    def __eq__(self, other):
        return self.rank_order == other.rank_order

    def __lt__(self, other):
        return self.rank_order < other.rank_order


class CardList(list):

    def __init__(self, card_list=None):
        if card_list is None:
            card_list = []
        super().__init__(card_list)

    def add_card(self, card):
        if isinstance(card, Card):
            self.append(card)
        else:
            raise TypeError("Can only add cards")

    def play_card(self, card):
        try:
            self.remove(card)
        except ValueError:
            print("Card not in list")
            raise
        else:
            return card


class Deck(CardList):

    def __init__(self):
        super().__init__()
        for suit in Card.suits:
            for rank in Card.ranks:
                self.add_card(Card(rank, suit))

    def shuffle(self):
        shuffle(self)

    def play_top_card(self):
        card = self.pop()
        return card

    def deal(self, num_players, num_cards):
        hands = [CardList() for _ in range(num_players)]
        for c in range(num_cards):
            for p in range(num_players):
                hands[p].add_card(self.play_top_card())
        return hands

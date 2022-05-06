from random import shuffle


class Card:
    suits = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, rank, suit):

        if rank in self.ranks:
            self.rank = rank
        else:
            raise TypeError("Invalid rank")
        if suit.upper() in self.suits.keys():
            self.suit = suit.upper()
        else:
            raise TypeError("Invalid suit")

    def __repr__(self):
        return f'Card <{self.rank} of {self.suits[self.suit]}>'

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        suit_list = list(self.suits)
        self_rank = (self.rank.index(self.rank), suit_list.index(self.suit))
        other_rank = (other.rank.index(other.rank), suit_list.index(self.suit))
        return self_rank < other_rank


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

import pytest
import random
from card_game import Card, CardList, Deck


@pytest.fixture
def my_card_list():
    return CardList([Card("A", "S"), Card("Q", "H"), Card("3", "D")])


class TestCard:
    def test_card(self):
        card_3h = Card("3", "H")
        card_as = Card("A", "S")
        assert repr(card_3h) == 'Card <Three of Hearts>'
        assert card_3h.rank_order == (1, 2)
        assert (card_as > card_3h)

    def test_invalid_card(self):
        with pytest.raises(ValueError) as rank_exc:
            Card("1", "S")
        with pytest.raises(ValueError) as suit_exc:
            Card("3", "A")
        assert "Invalid rank" in str(rank_exc.value)
        assert "Invalid suit" in str(suit_exc.value)


class TestCardList:
    def test_add_card(self):
        card_list = CardList()
        card_list.add_card(Card("3", "H"))
        card_list.add_card(Card("7", "S"))
        assert repr(card_list) == '[Card <Three of Hearts>, Card <Seven of Spades>]'

    def test_list_cards(self, my_card_list):
        assert repr(my_card_list) == '[Card <Ace of Spades>, Card <Queen of Hearts>, Card <Three of Diamonds>]'
        my_card_list.sort()
        assert repr(my_card_list) == '[Card <Three of Diamonds>, Card <Queen of Hearts>, Card <Ace of Spades>]'

    def test_play_card(self, my_card_list):
        my_card = my_card_list.play_card(Card("3", "D"))
        assert len(my_card_list) == 2
        assert my_card == Card("3", "D")
        with pytest.raises(ValueError):
            my_card_list.play_card(Card("J", "H"))


class TestDeck:
    @pytest.fixture
    def my_deck(self):
        random.seed(0)
        return Deck()

    def test_deck_shuffle(self, my_deck):
        assert len(my_deck) == 52
        assert my_deck[0] == Card('2', 'C')
        assert my_deck[-1] == Card('A', 'S')
        # The random shuffle is seeded in the my_deck fixture to always produce the same result
        my_deck.shuffle()
        top_card = my_deck.play_top_card()
        assert top_card == Card('K', 'D')
        assert len(my_deck) == 51

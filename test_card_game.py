from card_game import Card, CardSet


def test_card():
    card_3h = Card("3", "H")
    card_as = Card("A", "S")
    assert repr(card_3h) == 'Card <3 of Hearts>'
    # assert (card_as > card_3h)


def test_add_card():
    cs = CardSet()
    cs.add_card(Card("3", "H"))
    cs.add_card(Card("7", "S"))
    assert repr(cs) == '[Card <3 of Hearts>, Card <7 of Spades>]'


def test_play_card():
    assert False

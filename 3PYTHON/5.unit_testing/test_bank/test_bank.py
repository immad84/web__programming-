from bank import value

def test_correct_greeting():
    assert value('Hello, Immad') == 0

def test_fined_greeting():
    assert value('How are you, Immad') == 20
    assert value('What\'s up Immad') == 100
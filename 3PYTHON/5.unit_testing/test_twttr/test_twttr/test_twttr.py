from twttr import shorten

def test_upper_str():
    assert shorten('HELLO, WORLD') == 'HLL, WRLD'

def test_lower_str():
    assert shorten('hello, world') == 'hll, wrld'

def test_not_vowel_str():
    assert shorten('Shhh! Nth cwm crwth!') == 'Shhh! Nth cwm crwth!'

def test_numnber_str():
    assert shorten('007 James Bond 007') == '007 Jms Bnd 007'

def test_empty_str():
    assert shorten('') == ''

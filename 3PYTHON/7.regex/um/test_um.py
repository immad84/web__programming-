from um import count

def test_count_um():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('Um,') == 1

def test_count_um_multiple():
    assert count('Um, thanks, um...') == 2
    assert count('um, hello, um, world') == 2

def test_count_um_in_word():
    assert count('umbrella album um') == 1

def test_count_um_case_insensitive():
    assert count('UM, um, Um') == 3

def test_countno_um():
    assert count('This is a test sentence.') == 0

from plates import is_valid

def test_start_with_two_letters():
    assert is_valid('AA2222') == True
    assert is_valid('22AAAA') == False

def test_length_vanity_plate():
    # check correct length
    assert is_valid('AACC12') == True
    # check in-correct length
    assert is_valid('AACC1234') == False
    assert is_valid('AA') == True

def test_numbers_in_middle():
    assert is_valid('AA12CC') == False
    assert is_valid('AAA22A') == False

def test_first_number_on_plate():
    assert is_valid('AA0123') == False

def test_punctuation():
    assert is_valid('AA,?12') == False

def test_empty_str():
    assert is_valid('') == False

def test_all_numbers():
    assert is_valid('123456') == False

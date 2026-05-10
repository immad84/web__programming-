from numb3rs import validate

def test_validate_first_byte():
    assert validate('127.300.1.2') == False # testing first byte is in range

def test_validate_to_true():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('140.247.235.144') == True

def test_validate_to_false():
    assert validate('275.3.6.28') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False

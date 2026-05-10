from response import is_valid

def test_is_valid_valid_response():
    assert is_valid('malan@harvard.edu') == 'Valid'
    assert is_valid('immad.uddin84@gmail.com') == 'Valid'

def test_is_valid_invalid_response():
    assert is_valid('malan@@@harvard.edu') == 'Invalid'
    assert is_valid('immad.uddin84@gmail..com') == 'Invalid'
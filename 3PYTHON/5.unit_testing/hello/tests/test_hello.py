from hello import hello

def test_default():
    assert hello() == 'Hello, World'

def test_argument():
    assert hello('Immad') == 'Hello, Immad'

def test_several_arguments():
    for name in ['Immad', 'Shahbaz', 'Usama']:
        assert hello(name) == f'Hello, {name}'
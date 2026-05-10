from watch import parse

def test_parse_http():
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_parse_https():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_parse_without_youtube():
    assert parse('<iframe src="https://cs50.harvard.edu/python"></iframe>') == None

def test_parse_without_iframe():
    assert parse('https://www.youtube.com/embed/xvFZjo5PgG0') == None
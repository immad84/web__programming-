from seasons import get_age_words
from datetime import datetime

def test_get_minutes():
    dob = datetime(1999, 1, 1)
    today = datetime(2000, 1, 1)
    assert get_age_words(dob, today) == 'Five hundred twenty-five thousand, six hundred minutes'

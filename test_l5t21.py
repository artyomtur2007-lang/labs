from l5t21 import count_words
def test_empty_str():
    assert count_words("") == 0
def test_only_spacs():
    assert count_words(" ")==0
def test_any_amount():
    assert count_words("Привет всем это моя проверка")==5
def test_more_spcs():
    assert count_words("  привет  ")==1
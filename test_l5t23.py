from l5t23 import is_palindrome
def test_digits():
    assert is_palindrome(1221) is True
def test_str():
    assert is_palindrome('шалаш')is True
def test_not_pol():
    assert is_palindrome('hello') is False
def test_with_upper():
    assert is_palindrome('тОпОТ') is True
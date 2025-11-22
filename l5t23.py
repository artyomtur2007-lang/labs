def is_palindrome(value):
    s = str(value).lower()
    return s == s[::-1]
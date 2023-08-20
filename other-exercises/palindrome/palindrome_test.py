import palindrome


def test_is_palindrome():
    assert palindrome.is_palindrome("soros")
    assert palindrome.is_palindrome("torot")
    assert not palindrome.is_palindrome("chair")

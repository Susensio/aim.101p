def is_palindrome(word):
    first_letter = word[0].lower()
    last_letter = word[-1].lower()

    if len(word) < 2:
        return True
    elif first_letter == last_letter:
        return is_palindrome(word[1:-1])
    else:
        return False


def test_palindrome():
    assert is_palindrome("kayaK") is True
    assert is_palindrome("racecar") is True


def test_non_palindrome():
    assert is_palindrome("artificial intelligence") is False

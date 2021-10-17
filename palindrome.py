def palindrome_check(word):
    """
    returns if a given word is a palindrome. Works by triming the front
    and back of the word for every call as long as the letters are the same.

    word: the word to check.
    """
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome_check(word[1:-1])


def main():
    word = input("Please enter a word: ")
    print("'{}' is{} a palindrome".format(
        word, "" if palindrome_check(word) else " not"))


if __name__ == "__main__":
    main()

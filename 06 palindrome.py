def check_palindrome(text):
    text = text.upper().replace(" ","")
    middle = len(text) // 2
    for i in range(middle):
        if text[i] != text[::-1][i]:
            return False
    return True

if __name__ == '__main__':
    d = check_palindrome("kajak")
    print(d)
    d = check_palindrome("koralgol")
    print(d)
    d = check_palindrome("Kobyła ma mały bok")
    print(d)
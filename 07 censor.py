def censor(text, not_valid = ["Java", "C#", "Ruby", "PHP"]):
    temp = text.split()
    for i in range(len(temp)):
        if temp[i] in not_valid:
            temp[i] = "****"
    return ' '.join(temp)


if __name__ == '__main__':
    c = censor("Java is the best, but PHP is the bestest!")  # ;-)
    print (c)
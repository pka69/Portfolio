from collections import Counter 

def letters_count(text):
    sentence = text.replace(" ", "").lower()
    return Counter(sentence)

def letters_count_max(text):
    dic_of_letters = letters_count(text)
    return dic_of_letters.most_common(1)

def letters_count_max_all(text):
    dic_of_letters = letters_count(text)
    max_repeat = dic_of_letters.most_common(1)[0][1]
    max_letters = []
    for key in dic_of_letters.keys():
        if dic_of_letters[key] == max_repeat:
            max_letters.append(key)
    return max_repeat, max_letters

if __name__ == '__main__':
    sentence = "Toby znow jest zły"
    print(sentence)
    print(letters_count(sentence))
    print(letters_count_max(sentence))
    print(letters_count_max_all(sentence))
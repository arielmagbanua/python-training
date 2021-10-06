def is_palindrome(string: str) -> bool:
    string = string.lower().replace(" ", "")
    reversed_string = string[::-1]
    return string == reversed_string

def is_palindrome_string(string: str) -> bool:
    strings_list = string.split(' ')

    # get all the first letters
    first_letters = []
    for string in strings_list:
        first_letters.append(string[0])

    # transform to a string
    first_letters = ''.join(first_letters)

    return is_palindrome(first_letters)

def reverse_sentence(s: str) -> str:
    # determine the words
    words = []
    word_temp = []

    for char in s:
        if char.isupper():
            # new word therfore append the word_temp and reset it
            if len(word_temp) > 0:
                word = ''.join(word_temp)
                words.append(word)
            
            word_temp = []
            word_temp.append(char)
        else:
            word_temp.append(char)
    
    # add the last word
    if len(word_temp) > 0:
        word = ''.join(word_temp)
        words.append(word)

    # reverse each word
    words = [word[::-1] for word in words]

    # join to make one string
    return ''.join(words)

print(is_palindrome_string('test string test'))
print(reverse_sentence('ATest string!'))

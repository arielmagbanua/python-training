def is_palindrome(string: str) -> bool:
    string = string.lower().replace(" ", "")
    reversed_string = string[::-1]
    return string == reversed_string

def is_palindrome_string(string: str) -> bool:
    strings_list = string.split(' ')

    # get all the first letters
    first_letters = ''
    for string in strings_list:
        first_letters += string[0]

    return is_palindrome(first_letters)

def reverse_sentence(s: str) -> str:
    # determine the words
    words = {}
    word_temp = ''

    # index to mimic indicing for the words dictionary
    dict_index = 0
    for char in s:
        if char.isupper():
            # new word therfore add the word_temp and reset it
            if len(word_temp) > 0:
                dict_index+=1
                words[dict_index] = word_temp
            
            word_temp = ''
            word_temp += char
        else:
            word_temp += char
    
    # add the last word
    if len(word_temp) > 0:
        dict_index+=1
        words[dict_index] = word_temp

    # reverse each word and add to a string
    reversed_words = ''
    for word in words.values():
        reversed_words += word[::-1]

    return reversed_words

print(is_palindrome_string('test string test'))
print(reverse_sentence('ATest string!'))

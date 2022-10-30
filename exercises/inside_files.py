# Get number 1-5 input from the user
line_number = 0
while True:
    try:
        line_number = int(input())
    except ValueError:
        continue
    if line_number in range(1, 6):
        break

def strip_symbols(word):
    """Filters out symbols from the word.

    Returns:
        string: The stripped version of the word.
    """

    # filter out symbols from the word
    filtered = filter(str.isalnum, word)

    return ''.join(filtered)

def is_unique(reference_word, word_line):
    """Determines if the reference word unique to the line.

    Returns:
        boolean: Return true if unique otherwise false.
    """
    counter = 0

    for word in word_line:
        if strip_symbols(reference_word.lower()) == strip_symbols(word.lower()):
            # the reference word is equal or is a sub string to the current word
            counter += 1

    # this means that only one match
    # it means also that it match itself so technically the word is unique
    return counter == 1

# Open the text file
with open('tweets2.txt', 'r') as text_file:
    lines = text_file.readlines()

    # Assign line number per line
    if line_number == 1:
        word_line = lines[0].split()
    elif line_number == 2:
        word_line = lines[1].split()
    elif line_number == 3:
        word_line = lines[2].split()
    elif line_number == 4:
        word_line = lines[3].split()
    else:
        word_line = lines[4].split()

    # Initialize stopword and common word counter to 0
    stopword = 0
    common_word = 0
    unique_count = 0
    
    # Get the total number of stopword and common word
    for word in word_line:
        if len(strip_symbols(word)) <= 3:
            stopword += 1
        else:
            common_word += 1
        
        if is_unique(word, word_line):
            unique_count += 1

    # Get the overall number of words
    overall_count = len(word_line)

    # Initialize output to dictionary
    output_dict = {
                    f"'line': {line_number}, "
                    f"'s': {stopword}, "
                    f"'c': {common_word}, "
                    f"'u': {unique_count}, "
                    f"'o': {overall_count}"
    }

    # Printing the output
    print(output_dict)

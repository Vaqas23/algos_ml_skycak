def check_if_symmetric(text):
    for i in range(len(text)//2):
        if text[i] != text[-(i+1)]:
            return False
    return True


def convert_to_numbers(text):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    numArray = []
    text = text.lower()
    for letter in text:
        numArray.append(alphabet.index(letter))
    return numArray


def convert_to_letters(numArray):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    text = ""
    for num in numArray:
        text += alphabet[num]

    return text


def get_intersection(array1, array2):
    set1, set2 = set(array1), set(array2)
    shared_values = []
    for val in set1:
        if val in set2:
            shared_values.append(val)
    return shared_values


def get_union(array1, array2):  # Initally used no sets, much faster now
    shared_values = set()
    for num in array1:
        if num not in shared_values:
            shared_values.add(num)
    for num in array2:
        if num not in shared_values:
            shared_values.add(num)
    shared_values = list(shared_values)
    return shared_values


def count_characters(text):
    dictionary = dict()
    text = text.lower()
    for ch in text:
        if ch in dictionary:
            dictionary[ch] += 1
        else:
            dictionary[ch] = 1

    return dictionary

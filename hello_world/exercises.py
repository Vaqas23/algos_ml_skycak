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

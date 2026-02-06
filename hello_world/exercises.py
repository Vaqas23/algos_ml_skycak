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

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

# Above is from "ch1/intro_exercises.py"


def encode_string(text, a, b):
    number_form = convert_to_numbers(text)
    encoded_form = []
    for number in number_form:
        encoded_form.append((a * number) + 3)
    return encoded_form

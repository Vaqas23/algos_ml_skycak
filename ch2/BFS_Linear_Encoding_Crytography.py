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
        encoded_form.append((a * number) + b)
    return encoded_form


def decode_numbers(nums, a, b):
    function_applied = []
    for num in nums:
        function_applied.append((num-b)/a)

    for num in function_applied:
        if num < 0 or num > 26:
            return False
        elif num % 1 != 0:
            return False

    input_to_function = []
    for num in function_applied:
        input_to_function.append(int(num))

    return convert_to_letters(input_to_function)


def BFS_decorder(num):

    for a in range(1, 101):
        for b in range(0, 101):
            if decode_numbers(num, a, b) != False:
                print(f"{decode_numbers(num, a, b)},a = {a}, b = {b}")
    return "Done"


BFS_decorder([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717,
             241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751])

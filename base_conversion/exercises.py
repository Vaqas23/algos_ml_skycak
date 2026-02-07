
def binary_to_decimal(text):
    decimal_form = 0
    text = text[::-1]
    for i in range(len(text)):
        decimal_form += int(text[i]) * (2**i)

    return decimal_form


def hexadecimal_to_decimal(text):
    decimal_form = 0
    hexadecimal_reference = "0123456789ABCDEF"
    text = text[::-1]
    count = 0
    for i in text:
        decimal_form += hexadecimal_reference.index(i) * (16**count)
        count += 1

    return decimal_form


def decimal_to_binary(text):  # Only works for positive values
    integer_decimal = int(text)
    binary_form = ""
    if integer_decimal == 0:
        return "0"
    else:
        while integer_decimal != 1:
            if integer_decimal % 2 == 1:
                binary_form += "1"
            else:
                binary_form += "0"
            integer_decimal //= 2

    binary_form += "1"
    binary_form = binary_form[::-1]
    return binary_form


def decimal_to_hexadecimal(text):

    integer_decimal = abs(int(text))
    hexadecimal_form = ""
    hexadecimal_library = "0123456789ABCDEF"
    if integer_decimal == 0:
        return "0"
    else:
        while integer_decimal != 0:
            hexadecimal_form += hexadecimal_library[integer_decimal % 16]
            integer_decimal //= 16
    if int(text) < 0:
        hexadecimal_form += "-"

    hexadecimal_form = hexadecimal_form[::-1]

    return hexadecimal_form


def binary_to_hexadecimal(text):
    return decimal_to_hexadecimal(binary_to_decimal(text))

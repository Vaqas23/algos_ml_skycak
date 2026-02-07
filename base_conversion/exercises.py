
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


def decimal_to_binary(text):
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


print(decimal_to_binary("9"))


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

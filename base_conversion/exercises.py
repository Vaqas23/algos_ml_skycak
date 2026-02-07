
def binary_to_decimal(text):
    decimal_form = 0
    text = text[::-1]
    for i in range(len(text)):
        decimal_form += int(text[i]) * (2**i)

    return decimal_form

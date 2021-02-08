import eel
from bincal import *

@eel.expose
def calc(num1, num2, value1, value2, operation):

    if value1 == "Binary":
        num1 = bincal.convert_bin_to_den(num1)
    elif value1 == "Hex":
        num1 = bincal.convert_hex_to_den(num1)
    else:
        num1 = int(num1)
    if value2 == "Binary":
        num2 = bincal.convert_bin_to_den(num2)
    elif value2 == "Hex":
        num2 = bincal.convert_hex_to_den(num2)
    else:
        num2 = int(num2)

    if operation == "+":
        output_den = num1+num2
        output_bin = bincal.convert_den_to_bin(num1+num2)
        output_hex = bincal.convert_den_to_hex(num1 + num2)
    elif operation == "-":
        output_den = num1-num2
        output_bin = bincal.convert_den_to_bin(num1-num2)
        output_hex = bincal.convert_den_to_hex(num1-num2)
    elif operation == "*":
        output_den = num1 * num2
        output_bin = bincal.convert_den_to_bin(num1 * num2)
        output_hex = bincal.convert_den_to_hex(num1 * num2)
    elif operation == "/":
        try:
            output_den = f"{num1 // num2} Remainder {num1%num2}"
            output_bin = f"{bincal.convert_den_to_bin(num1 // num2)} Remainder {bincal.convert_den_to_bin(num1%num2)}"
            output_hex = f"{bincal.convert_den_to_hex(num1 // num2)} Remainder {bincal.convert_den_to_hex(num1%num2)}"
        except ZeroDivisionError:
            output_den = "Undefined"
            output_bin = "Undefined"
            output_hex = "Undefined"
    eel.output(output_den, output_bin, output_hex)


eel.init('www')
eel.start('index.html', block = False)

while True:

    eel.sleep(1)

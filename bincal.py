class bincal:

    @staticmethod
    def convert_bin_to_den(binary):
        return int(binary, 2)

    @staticmethod
    def convert_den_to_bin(num):
        if num >= 0:
            binary = bin(num)
            return binary[2:]
        else:
            binary = bin(num)
            return f"-{binary[3:]}"

    @staticmethod
    def convert_bin_to_hex(binary):
        num = bincal.convert_bin_to_den(str(binary))
        return bincal.convert_den_to_hex(num).upper()

    @staticmethod
    def convert_den_to_hex(num):
        if num >= 0:
            hexadecimal = hex(num)
            return hexadecimal[2:].upper()
        else:
            hexadecimal = hex(num)
            return f"-{hexadecimal[3:]}".upper()

    @staticmethod
    def convert_hex_to_den(num):
        return int(num,16)

    @staticmethod
    def convert_hex_to_bin(num):
        den = bincal.convert_hex_to_den(num)
        return bincal.convert_den_to_bin(den)

    @staticmethod
    def check_for_bin(string):
        string = list(string)
        for i in string:
            if not (i == "0" or i == "1"):
                return False
        else:
            return True

    @staticmethod
    def add(num1, num2):
        return str(bin(int(num1, 2) + int(num2, 2)))[2:]

    @staticmethod
    def subtract(num1, num2):
        if num1 < num2:
            return f"-{str(bin(int(num1, 2) - int(num2, 2)))[3:]}"
        else:
            return str(bin(int(num1, 2) - int(num2, 2)))[2:]

    @staticmethod
    def multiply(num1, num2):
        return str(bin(int(num1, 2) * int(num2, 2)))[2:]

    @staticmethod
    def divide(num1, num2):

        return str(bin(int(num1, 2) // int(num2, 2)))[2:], str(bin(int(num1, 2) % int(num2, 2)))[2:]
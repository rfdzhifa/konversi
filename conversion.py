
def string_to_binary(s):
    num = int(s)
    return bin(num)[2:]

def string_to_octal(s):
    num = int(s)
    return oct(num)[2:]

def string_to_hexadecimal(s):
    num = int(s)
    return hex(num)[2:]

def string_to_ascii(s):
    ascii_list = []
    for char in s:
        ascii_list.append(ord(char))
    return ascii_list


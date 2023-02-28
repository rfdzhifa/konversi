from conversion import string_to_decimal
from conversion import string_to_binary
from conversion import string_to_octal
from conversion import string_to_hexadecimal
from conversion import string_to_ascii

def menu():
    try:
        print('=== Konversi ===')
        print('1. Desimal')
        print('2. Biner')
        print('3. Okta')
        print('4. Hexadecimal')
        print('5. ASCII')
        print('0. Exit')

        pilihan = int(input('masukan pilihan konversi : '))
        print('')

        if pilihan == 1:
            value = int(input('masukkan angka : '))
            decimal_string = string_to_decimal(value)
            print(decimal_string)

        elif pilihan == 2:
            value = int(input('masukkan angka : '))
            binary_string = string_to_binary(value)
            print(binary_string)

        elif pilihan == 3:
            value = int(input('masukkan angka : '))
            octal_string = string_to_octal(value)
            print(octal_string)

        elif pilihan == 4:
            value = int(input('masukkan angka : '))
            hexadecimal_string = string_to_hexadecimal(value)
            print(hexadecimal_string)

        elif pilihan == 5:
            value = int(input('masukkan angka : '))
            ascii_list = string_to_ascii(value)
            print(ascii_list)

        elif pilihan == 0:
            exit()

        else:
            print("pilihan tidak tersedia")


    finally:
        print('')

if __name__ == "__main__":
    while (True):
        menu()
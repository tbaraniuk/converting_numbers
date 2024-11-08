number_formats = '0123456789ABCDEF'


def check_number(num: str, base: int) -> bool:
    for i in num:
        if i not in number_formats or number_formats.index(i) >= base:
            return False

    return True



def convert_decimal_to_any_base(num: int, base: int = 10) -> str:
    if base == 10:
        return num

    res = ''
    i = num

    while i != 0:
        res += number_formats[int(i % base)]
        i = i // base

    return res[::-1]


def convert_number_to_decimal(num: str, num_base: int = 10) -> int:
    res = 0
    num_str = num[::-1]
    for i in range(len(num_str)):
        res += number_formats.index(num_str[i]) * (num_base ** i)

    return res


def main():
    data = ''

    while True:
        data = input('Enter your number to convert in format "num x base" like (10x2) or "exit" to exit from a program: ')

        if data == 'exit':
            return

        data_arr = data.split('x')
        num = data_arr[0]

        base = data_arr[1] if len(data_arr) == 2 else '10'

        if not num or not base or not base.isdigit() or not check_number(num, int(base)):
            data = input('Please, enter valid number to convert in format "num x base" like (10x2) or "exit" to exit from a program: ')

        format = input('Write base in which you want to convert your number: ')

        if not format.isdigit() or int(format) > 16 or int(format) < 2:
            format = input('Please, write valid base in which you want to convert your number (2/10): ')

        decimal_num = convert_number_to_decimal(num, int(base))

        print(convert_decimal_to_any_base(decimal_num, int(format)))


if __name__ == '__main__':
    main()
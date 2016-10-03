import sys

times = 0

# 初始化一个字母表
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

plain = input("Please input your plain text: ")
value = input("Please input your key(included negatives): ")

try:
    value = int(value)
except ValueError:
    print("Please input an integer.")
    sys.exit()

secret_list = list(plain)
secret_list_len = len(secret_list)

print("")
print("secret: ", end='')

while times < secret_list_len:
    times = times + 1

    try:
        num = int(alphabet.index(plain[times - 1]) + int(value))
        output = alphabet[num]
    except ValueError:
        try:
            num = int(alphabet_upper.index(plain[times - 1]) + int(value))
            output = alphabet_upper[num]
        except IndexError:
            if num > 25:
                num = int(num % 26)
            if num < -25:
                num = int(-(-num % 26))
            output = alphabet_upper[num]
        except ValueError:
            output = plain[times - 1]
    except IndexError:
        if num > 25:
            num = int(num % 26)
        if num < -25:
            num = int(-(-num % 26))
        output = alphabet[num]

    print(output, end='')

print("")
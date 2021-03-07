import string
import random

symbols = ['@', '#', '$', '%', '#', '[', ']']

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

# with open('/opt/rockyou.txt', 'r') as rockyou:
#rockyou_list = rockyou.readlines()
# print(rockyou_list)


def get_lengths():
    global lengthlower, lengthupper, lengthsymbols

    lengthlower = int(input(
        "Please input the number of lowercase letters in password: "))
    lengthupper = int(
        input("Please input the number of uppercase in password: "))
    lengthsymbols = int(input(
        "Please input the number of symbols in the password - up to 7:  "))

    if lengthlower > 26:
        print('Please select a number lower than 26')
        get_lengths()
    elif lengthlower > 26:
        print('Please select a number lower than 26')
        get_lengths()
    elif lengthsymbols > 7:
        print('Please select a number lower than 7')
        get_lengths()
    else:
        pass

    return {'lengthlower': lengthlower, 'lengthupper': lengthupper, 'lengthsymbols': lengthsymbols}


get_lengths()


def symbol():

    global random_symbol

    symbol_list = random.sample(symbols, lengthsymbols)
    symbol_list_joined = ''.join(symbol_list)
    random_symbol = symbol_list_joined.split(',')
    # print(random_symbol)
    return random_symbol


def get_lower():

    global random_lower

    lower_list = random.sample(lower, lengthlower)
    lower_list_joined = ''.join(lower_list)
    random_lower = lower_list_joined.split(',')
    # print(random_lower)
    return random_lower


def get_upper():

    global random_upper

    upper_list = random.sample(upper, lengthupper)
    upper_list_joined = ''.join(upper_list)
    random_upper = upper_list_joined.split(',')
    # print(random_upper)
    return random_upper


def main():

    symbol()
    get_lower()
    get_upper()

    lists = random_lower + random_upper + random_symbol

    password = ''.join(lists)

    print(password)


if __name__ == "__main__":
    main()

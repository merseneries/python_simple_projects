import os
from _local_package import get_digit_input


def get_random():
    import random
    return random.randint(0, 6)


def main():
    while True:
        num_dice = get_digit_input("Number of dice: ")
        if num_dice > 0:
            break
        print("Number of dice must be > 0")

    print("--Table of dice--")
    for i in range(num_dice):
        if i % 5 == 0:
            print(end="\n")
        print("{:3}".format(get_random()), end=" ")

    str_input = input("\n\nTry again?(y/n)\n")
    if str_input == "y":
        os.system("cls")
        main()


if __name__ == '__main__':
    main()

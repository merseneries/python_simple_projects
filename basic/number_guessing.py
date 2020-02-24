import random
import os
from _local_package import get_digit_input

COUNT_TRY = 5
line = "-" * 25


def main():
    range_input = get_digit_input("Choose digit for range. Starting from 0 to ")
    secret_dig = random.randint(0, int(range_input))
    for i in range(COUNT_TRY, -1, -1):
        dig_input = get_digit_input("What digit I have in mind?\n")

        if dig_input == secret_dig:
            print("Congratulation you won.", "\n" + line)
            break
        else:
            print("Secret is greater" if dig_input < secret_dig else "Secret is smaller")
        print("Try:", i, "\n" + line)

    else:
        print("You lose.")

    str_input = input("Try again?(y/n)\n")
    if str_input == "y":
        os.system("cls")
        main()


if __name__ == '__main__':
    main()

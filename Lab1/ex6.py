def palindrome(number):
    number_copy = number
    ogl = 0

    while number:
        digit = number % 10
        ogl = ogl * 10 + digit
        number = number // 10

    if number_copy == ogl:
        return True
    else:
        return False


def main():

    number = 12341143121

    if palindrome(number):
        print("Number %d is a palindrome" % number)
    else:
        print("Number %d is NOT a palindrome" % number)

    return 0


if __name__ == "__main__":
    main()

#   Varianta 2
#   num_str = str(number)
#   Comparam stringul original cu inversul
#   return num_str == num_str[::-1]
#   number = int(input("Enter a number: "))

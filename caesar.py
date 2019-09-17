alphanumswap = {"a" : 0,  "b" : 1, "c" : 2, "d" : 3, "e" : 4,
                "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9,
                "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14,
                "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19,
                "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24,
                "z" : 25}


def alphabet_position(letter):
    return alphanumswap[letter.lower()]


def rotate_character(char, rot):
    if char.isupper():
        isup = True
    elif char.islower():
        isup = False
    else:
        return char
    i = alphabet_position(char)
    new_char = (i + rot) % 26
    #j = key in dictionary (letter)
    #k = value in dictionary (number)
    for j, k in alphanumswap.items():
        if new_char == k:
            if isup == True:
                return j.upper()
            else:
                return j


def rotate_string(text, rot):
    new_string = ""
    for i in text:
        if i.isalpha():
            char = rotate_character(i, rot)
            # print(char)
            new_string += char
        else:
            new_string += i
    return new_string


def main():
   message = input("What is your message:\n")
   rotate = int(input("What rotation would you like:\n"))
   print(rotate_string(message, rotate))


if __name__ == "__main__":
    main()

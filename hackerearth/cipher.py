# chiper
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cipher-1/
s = input()
k = int(input())

final_list = []


def upper_character(ascii):
    j = k % 26
    update = j + ascii
    if update > 90:
        a = update - 91
        update = 65 + a
    return update


def lower_character(ascii):
    j = k % 26
    update = j + ascii
    if update > 122:
        a = update - 123
        update = 97 + a
    return update


def numbers(ascii):
    j = k % 10
    update = j + ascii
    if update > 57:
        a = update - 58
        update = 48 + a
    return update


def main():
    lst = []
    for i in range(0, len(s)):
        ascii = ord(s[i])

        if ascii > 64 and ascii < 91:
            final_list.append(chr(upper_character(ascii)))

        elif ascii > 96 and ascii < 123:
            final_list.append(chr(lower_character(ascii)))

        elif ascii >= 48 and ascii <= 58:
            final_list.append(chr(numbers(ascii)))
        else:
            final_list.append(chr(ascii))

    print("".join(final_list))


if __name__ == '__main__':
    main()

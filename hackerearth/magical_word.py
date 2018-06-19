#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/magical-word/
prime_numbers = []


def is_prime(number):
    if number == 1:
        return True

    if number > 1:
        for _ in range(2, number):
            if (number % _) == 0:
                return False
        return True
    else:
        return False


def get_nearest_prime_number(number):

    for i in range(0, len(prime_numbers)):
        if number == prime_numbers[i]:
            return number
        elif number < prime_numbers[i] and i ==0:
            return prime_numbers[i]
        elif i == len(prime_numbers)-1 and number > prime_numbers[i]:
            return prime_numbers[i]
        elif number > prime_numbers[i] and number < prime_numbers[i+1]:
            left_diff = number - prime_numbers[i]
            right_diff = prime_numbers[i+1] - number

            if right_diff < left_diff:
                return prime_numbers[i+1]
            else:
                return prime_numbers[i]


def get_prime_numbers():

    for n in range(65, 91):
        if is_prime(n):
            prime_numbers.append(n)

    for n in range(97, 123):
        if is_prime(n):
            prime_numbers.append(n)


def main():
    t = int(input())

    get_prime_numbers()
    for _ in range(t):
        lst = []
        n = int(input())
        s = input()
        for i in range(0, n):
            ascii_ = ord(s[i])
            lst.append(chr(get_nearest_prime_number(ascii_)))

        print("".join(lst))


if __name__ == '__main__':
    main()





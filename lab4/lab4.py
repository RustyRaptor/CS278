def is_prime(n):
    if n <= 0 or n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def hundred_squares():
    for number in range(100):
        yield number ** 2


def check():
    for n in range(3, 10000, 2):
        for cnt, square in enumerate(hundred_squares()):
            if is_prime((n - (square * 2))):
                break
            elif cnt >= 99:
                print("The smallest one is", n)
                return


check()

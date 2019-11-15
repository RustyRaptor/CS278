def sum1(n):
    # base case
    if n == 0:
        return 2 ** 0

    # recursive case
    return 2 ** n + sum1(n - 1)


def sum2(n):
    # base case
    if n == 1:
        return 2

    # recursive case
    return (n * (n + 1)) + (sum2(n - 1))


user_n = int(input("Please enter the value of n: "))

print("The value of the 1st summation is", sum1(user_n))
print("The value of the 2nd summation is", sum2(user_n))


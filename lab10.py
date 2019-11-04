def summation(n):
    if n == 1:
        return 2
    inductive = summation(n - 1)

    last_term = 2 * n
    return inductive + last_term


print(summation(4))

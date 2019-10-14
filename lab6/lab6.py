n = int(input("Please enter the value of n: "))
Y = list(range(1, n + 1))


def function_generator(target):
    num = 0
    for anum, a in enumerate(target):
        for bnum, b in enumerate(target):
            for cnum, c in enumerate(target):
                num += 1
                yield (a, b, c, num)


def numstr(num, x):
    return "f" + str(num) + "(" + str(x) + ")="


def is_1to1(a, b, c):
    if a != b != c != a:
        return True
    else:
        return False


def is_onto(a, b, c, target):
    output_set = {a, b, c}
    target_set = set(target)

    if len(target) > 3:
        return False
    if output_set == target_set:
        return True
    else:
        return False


def is_biject(a, b, c, target):
    if is_onto(a, b, c, target) and is_1to1(a, b, c):
        return True
    else:
        return False


def get_truths(a, b, c, target):
    return is_1to1(a, b, c), is_onto(a, b, c, target), is_biject(a, b, c, target)


def print_funcs(target):
    count_oto = 0
    count_onto = 0
    count_bi = 0
    for i in function_generator(target):
        a, b, c, num = i
        oto, onto, bi = get_truths(a, b, c, target)
        if oto:
            count_oto += 1
        if onto:
            count_onto += 1
        if bi:
            count_bi += 1
        print(
            numstr(num, "a") + str(a),
            numstr(num, "b") + str(b),
            numstr(num, "c") + str(c))
        print("One-To-One: ", oto)
        print("Onto: \t\t", onto)
        print("Bijection:  ", bi, end="\n\n")


print_funcs(Y)

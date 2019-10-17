Y = list(range(1, int(input("Please enter the value of n: ")) + 1))


def function_generator(targ):
    num = 0
    for a in targ:
        for b in targ:
            for c in targ:
                num += 1
                yield (a, b, c, num)


def numstr(num, x):
    return "f" + str(num) + "(" + str(x) + ")="


def is_1to1(a, b, c):
    if a != b != c != a:
        return True
    else:
        return False


def is_onto(a, b, c, targ):
    output_set = {a, b, c}
    targ_set = set(targ)

    if len(targ) > 3:
        return False
    if output_set == targ_set:
        return True
    else:
        return False


def is_biject(a, b, c, targ):
    if is_onto(a, b, c, targ) and is_1to1(a, b, c):
        return True
    else:
        return False


def get_truths(a, b, c, targ):
    return is_1to1(a, b, c), is_onto(a, b, c, targ), is_biject(a, b, c, targ)


def print_funcs(targ):
    count_oto = 0
    count_onto = 0
    count_bi = 0
    for i in function_generator(targ):
        a, b, c, num = i
        oto, onto, bi = get_truths(a, b, c, targ)
        if oto:
            count_oto += 1
        if onto:
            count_onto += 1
        if bi:
            count_bi += 1
        print("=" * 10, "FUNCTION", num, "=" * 10)
        print(
            numstr(num, "a") + str(a),
            numstr(num, "b") + str(b),
            numstr(num, "c") + str(c))
        print("One-To-One: ", oto)
        print("Onto: \t\t", onto)
        print("Bijection:  ", bi, end="\n\n")


print_funcs(Y)

def truth_gen(vars_count):
    """
    Generate a 2D list of truth values for N variables
    :param vars_count: Number of variables in the proposition
    :return: A 2d list of all the possible values for the variables
    """
    rows = 2 ** vars_count
    table = []
    bin_to_str = {
        '0': 'F',
        '1': 'T',
        ' ': 'F'
    }
    for i in range(rows):
        bins = "{0:>{1}}".format("{0:b}".format(i), vars_count)
        table.append([])
        for j, val in enumerate(bins):
            table[i].append(bin_to_str[val])
    return table


# Logical operators
def _not(i):
    return 'T' if i is 'F' else 'F'


def _or(i, j):
    return 'T' if i is 'T' or j is 'T' else 'F'


def _and(i, j):
    return 'T' if i is 'T' and j is 'T' else 'F'


def impl(i, j):
    return 'F' if i is 'T' and j is 'F' else 'T'


# Propositions
def prop1(args=None):
    if args is None:
        args = [0, 0, 0]
    p, q, r = tuple(args)
    return _and((impl(_not(p), q)), (impl(r, p))), "(~p → q) and (r → p)"


def prop2(args=None):
    if args is None:
        args = [0, 0, 0]
    p, q, r = tuple(args)
    return _and((_or(p, _not(q))),
                (_or(r, _not(impl(p, q))))), "(p or (~q)) and (r or  ~(p → q))"


def prop3(args=None):
    if args is None:
        args = [0, 0]
    p, q = tuple(args)
    return impl(p, (impl((_not(_and(p, _not(q)))),
                         (_and(p, q))))), "(p or (~q)) and (r or  ~(p → q))"


def prop4(args=None):
    if args is None:
        args = [0, 0]
    p, q = tuple(args)
    return _and((_and(p, (impl(p, q)))),
                (_not(q))), "(p or (~q)) and (r or  ~(p → q))"


def apply_prop(prop_function, vars_count):
    """
    Function to apply proposition functions to a truth table
    :param prop_function: a proposition function to apply
    :param vars_count: the number of variables for the proposition
    """
    args = [truth_gen(vars_count)]
    t_count = 0
    prop_type = ""
    print("p", "q", "r" if vars_count >= 3 else "", prop_function()[1])
    for i in truth_gen(vars_count):
        print(*i[0:], "{0:>{1}}".format(prop_function(i[:])[0],
                                        len(prop_function()[1]) / 2))
        if prop_function(i[:])[0] is 'T':
            t_count += 1
    f_count = 2 ** vars_count - t_count
    if t_count == 2 ** vars_count:
        prop_type = "a tautology"
    elif t_count == 0:
        prop_type = "a contradiction"
    else:
        prop_type = "neither a Tautology nor a Contradiction"

    print("Truths:", t_count, "\n", "\rFalsehoods:", f_count, "\n",
          "\rThe proposition is", prop_type, "\n", "_"*20)


# Main code to run all the propositions.
props = [prop1, prop2, prop3, prop4]

for key, prop in enumerate(props):
    print("Proposition", key + 1)
    apply_prop(prop, (3 if key <= 1 else 2))

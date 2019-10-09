import itertools


def bin_count(size):
    for i in itertools.product([0, 1], repeat=size):
        yield i


size_of = int(input("Please enter the size of S: "))
set_A = [char for char in input("Please enter the elements of S: ")]


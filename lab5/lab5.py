import itertools


def bin_count(size):
    for i in itertools.product([0, 1], repeat=size):
        yield i


size_of = int(input("Please enter the size of S: "))
set_A = [int(char) for char in input("Please enter the elements of S: ")]
N = int(input("Please enter the number N: "))
all_subsets = []
for binary in bin_count(len(set_A)):
    indices = [i for i, j in enumerate(binary) if j == 1]
    subset = []
    for index in indices:
        subset.append(set_A[index])
    all_subsets.append(subset)
count = 0
for cnt, sub in enumerate(all_subsets):
    if sum(sub) == N:
        tail = ","
        count += 1
    else:
        tail = " "
    print(sub if sum(sub) == N else "", end=tail)

print("there are", count, "subsets that sum up to ", N)
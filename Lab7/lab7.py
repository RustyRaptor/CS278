import itertools

values = []


def bin_count(size):
    for b in itertools.product([0, 1], repeat=size):
        yield b


bin_list = list(bin_count(3))
bin_list.reverse()
print(
    "This program finds Boolean expressions (in CNF and/or DNF)\n that have a "
    "given input/output table")
print("Please enter values (0 or 1) for each row of the input/output table.")

for i in bin_list:
    print("p=", i[0], ", q=", i[1], ", r=", i[2], ".")
    values.append(input(" Truth value is (1/0): "))
    print()

print("DNF expression for the input/output table is" if "1" in values else "")
for idx, val in enumerate(values):
    if val == "1":
        vals = bin_list[idx]
        p = "p" if vals[0] == 1 else "p'"
        q = "q" if vals[1] == 1 else "q'"
        r = "r" if vals[2] == 1 else "r'"
        plus = " +" if idx != len(values) - 1 else " "
        print(p + q + r + plus, end=" ")

print("\nCNF expression for the input/output table is" if "0" in values
      else "")
for idx, val in enumerate(values):
    if val == "0":
        vals = bin_list[idx]
        p = "(p+" if vals[0] == 0 else "(p'+"
        q = "q+" if vals[1] == 0 else "q'+"
        r = "r)" if vals[2] == 0 else "r')"
        print(p + q + r + " ", end=" ")

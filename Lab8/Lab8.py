vals = input("Please enter values of a, b, c, and M in this order (separated "
             "by spaces): ")

vals = vals.split(" ")
vals = [int(x) for x in vals]

begin_cycle = False
flag = 0
cycles = 0
start = vals[2]
start2 = vals[2]
for i in range(0, vals[3] - 1):
    if begin_cycle:
        cycles += 1
        if flag == start:
            begin_cycle = False
            break
    if i == vals[3] / 4:
        flag = start
        begin_cycle = True

    e = "\n" if (i + 1) % 10 == 0 and i > 0 else " "
    start = (vals[0] * start + vals[1]) % vals[3]

for j in range(0, 100):
    e = "\n" if (j + 1) % 10 == 0 and j > 0 else " "
    print(start2, end=e)
    start2 = (vals[0] * start2 + vals[1]) % vals[3]

print("\nCycle length is", cycles)

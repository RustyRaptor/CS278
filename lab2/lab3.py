domain = list(map(int, input().split(" ")))
a, b, c, d, = True, False, False, True
for x in domain:
    if x < 0 and x % 2 is not 0:
        a = False
    if (x < 0 and x % 2 is 0) or (not (x < 0) and x % 2 is 0):
        b = True
    if x < 0 and x % 2 is 0:
        c = True
    if (x - 1) % 3 is not 0 or (x - 1) % 2 is not 0:
        d = False
print("\na) is", a, "\nb) is", b, "\nc) is ", c, "\nd) is", d)

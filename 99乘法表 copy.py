print("99乘法表口诀")
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print("%d x %d = %d" % (b, a, (a * b)), end="  ")
        b += 1
    a += 1
    print("")

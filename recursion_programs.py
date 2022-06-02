def factorials(n):
    if n==1:
        return n
    else:
        return n*factorials(n-1)

print(factorials(6))


def fanc(n):
    if n== 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fanc(n-1) + fanc(n-2)

print(fanc(7))

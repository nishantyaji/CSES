n = int(input().strip())


def recur(x):
    if x == 1:
        print(1, end='')
        return
    print(x, end=' ')
    if x % 2 == 0:
        recur(x // 2)
    else:
        recur(3 * x + 1)


recur(n)

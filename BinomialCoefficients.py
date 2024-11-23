base = 1000000007

num_test = int(input().strip())
for _ in range(num_test):
    [a, b] = list(map(int, input().strip().split()))
    x = min(a - b, b)

    cntr = {}
    for i in range(2, x + 1):
        r = a % i
        if (a - r) not in cntr:
            cntr[a - r] = i
        else:
            cntr[a - r] = cntr[a - r] * i

    res = 1
    for bx in range(1, x + 1):
        res *= (a + 1 - bx)
        if (a + 1 - bx) in cntr:
            res //= cntr[a + 1 - bx]
        res = (res % base)
    print(res)

base = 1000000007

num_test = int(input().strip())
for _ in range(num_test):
    [a, b] = list(map(int, input().strip().split()))
    x = min(a - b, b)
    res = 1
    num = 1
    den = 1
    for i in range(1, x + 1):
        num = (num * (a + 1 - i)) % base
        den = (den * i) % base
    res = (num * pow(den, -1, base)) % base
    print(res)

n = int(input().strip())
for _ in range(n):
    r, c = list(map(int, input().strip().split()))
    l = max(r, c)

    res = -1
    if l == r and l == c:
        res = (l ** 2 + 1 + (l - 1) ** 2) // 2
    elif l == r:
        res = (l - 1) ** 2 + c if l % 2 == 1 else l ** 2 - (c - 1)
    else:
        res = (l - 1) ** 2 + r if l % 2 == 0 else l ** 2 - (r - 1)
    print(res)

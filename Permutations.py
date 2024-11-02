import sys

n = int(input().strip())
if n <= 4:
    if n == 4:
        print("2 4 1 3")
    elif n == 1:
        print("1")
    else:
        print("NO SOLUTION")
    sys.exit()
res = []
if n % 2 == 0:
    for i in range(n // 2):
        res.append(1 + i)
        res.append(i + (n // 2) + 1)

else:
    res = [1 + n // 2]
    for i in range(n // 2):
        res.append(1 + i)
        res.append(i + (n // 2) + 2)

print(*res)

n = int(input().strip())


def recur(x):
    if x == 1:
        return ["0", "1"]
    res = recur(x - 1)
    return list(map(lambda x: "0" + x, res)) + list(map(lambda x: "1" + x, res[::-1]))


for y in recur(n):
    print(y)

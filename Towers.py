import bisect

n = int(input().strip())
k = list(map(int, input().strip().split()))

tops = []
for y in k:
    if not tops or y >= tops[-1]:
        tops.append(y)
        continue

    idx = bisect.bisect_right(tops, y)
    tops[idx] = y

print(len(tops))

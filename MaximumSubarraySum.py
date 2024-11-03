import sys

_ = input()
x = list(map(int, input().strip().split()))

cur_max_sum, max_sum = -sys.maxsize, -sys.maxsize
for y in x:
    cur_max_sum = max(cur_max_sum + y, y)
    max_sum = max(max_sum, cur_max_sum)

print(max_sum)

import math
n = int(input().strip())
p = list(map(int, input().strip().split()))

p.sort()
# choose median, not mean
# (you can test and prove this for odd length)
# (for even length, choose any number in the range of the mid 2 elements)
print(sum([abs(i - p[n//2]) for i in p]))

import sys

n = int(input().strip())
x = list(map(int, input().strip().split()))

x.sort()
if x[0] > 1:
    print(1)
    sys.exit()

run_sum = x[0]
x += [sys.maxsize]
for i in range(1, len(x)):
    if run_sum + 1 < x[i]:
        print(run_sum+1)
        sys.exit()
    else:
        run_sum += x[i]


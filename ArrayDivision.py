import sys

[n, k] = list(map(int, input().strip().split()))
x = list(map(int, input().strip().split()))

if n == k:
    print(max(x))
    sys.exit()
if k == 1:
    print(sum(x))
    sys.exit()

suffix = [0] * n
run_sum = 0
for i in range(n - 1, -1, -1):
    run_sum += x[i]
    suffix[i] = run_sum


def solve(rr):
    divs, run_sum = 0, 0
    for idx, i in enumerate(x):
        if run_sum + i > rr:
            divs += 1
            if divs == k - 1:
                return not (suffix[idx] > rr)
            run_sum = i
            # The following 2 lines of code is required for the corner case
            # [n,k] = [4,3], x = [1 2 4 3]
            # If the individual elem is greater than rr
            if run_sum > rr:
                return False
            continue
        run_sum += i
    if divs < rr:
        return True


s, e = sum(x) // len(x), sum(x)
solved = []
while s <= e:
    mid = (s + e) // 2
    if solve(mid):
        solved.append(mid)
        e = mid - 1
    else:
        s = mid + 1

print(min(solved))

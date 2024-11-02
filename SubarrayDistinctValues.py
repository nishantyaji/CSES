[n, k] = list(map(int, input().strip().split()))
x = list(map(int, input().strip().split()))

# note that the right is initialized to -1
# so that we can increment by 1
# and consume (0th) element in an 0-indexed array
res, right, my_dict = 0, -1, {}


def add_(rr):
    if rr not in my_dict:
        my_dict[rr] = 0
    my_dict[rr] += 1


def rem_(rr):
    if rr in my_dict:
        my_dict[rr] -= 1
        if my_dict[rr] == 0:
            del my_dict[rr]


for left in range(n):
    while right < n and len(my_dict) <= k:
        right += 1
        if right < n:
            add_(x[right])
    res += (right - left)
    rem_(x[left])
print(res)

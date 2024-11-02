_ = input()
a = list(map(int, input().strip().split()))

stack, res = [], []
for i, ax in enumerate(a):
    while stack and stack[-1][0] >= ax:
        stack.pop()
    res.append(0 if not stack else stack[-1][1])
    stack.append((ax, i+1))
print(*res)

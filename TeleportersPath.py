import collections
import sys

[n, m] = list(map(int, input().strip().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().strip().split())))

adj = collections.defaultdict(collections.deque)
in_degree = collections.defaultdict(int)
out_degree = collections.defaultdict(int)
for s, e in edges:
    adj[s].append(e)
    in_degree[e] += 1
    out_degree[s] += 1

num_plus1, num_minus1 = 0, 0
for i in range(1, n + 1):

    if out_degree[i] - in_degree[i] == 1:
        num_plus1 += 1
    elif out_degree[i] - in_degree[i] == -1:
        num_minus1 += 1
    elif out_degree[i] - in_degree[i] == 0:
        pass
    else:
        print("IMPOSSIBLE")
        sys.exit()

if num_minus1 + num_plus1 > 0 and (out_degree[1] - in_degree[1] != 1 or out_degree[n] - in_degree[n] != -1):
    print("IMPOSSIBLE")
    sys.exit()

for i in range(2, n):
    if out_degree[i] != in_degree[i]:
        print("IMPOSSIBLE")
        sys.exit()

trail = []

# Hierholzer's Algorithm
start = 1
stack = [start]
while stack:
    nxt = stack[-1]
    if adj[nxt]:
        nxt2 = adj[nxt].popleft()
        stack.append(nxt2)
    else:
        trail.append(nxt)
        stack.pop()
    if len(trail) > m + 1:
        # Ideally you would not be requiring this. But this results in TLEs
        # So stop the algo when the length of the tour becomes larger than
        # the value expected
        print("IMPOSSIBLE")
        sys.exit()

trail.reverse()

cnt = 0
for k in adj.keys():
    if not adj[k] or len(adj[k]) == 0:
        cnt += 1

if len(trail) == m + 1 and trail[-1] == n and cnt == len(adj):
    print(*trail)
else:
    print("IMPOSSIBLE")

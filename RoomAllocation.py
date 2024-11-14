import heapq
from collections import deque

"""
Python solutions do not fit the memory and time constraints
even if they adhere the suggested algo to the word.
"""

num_rooms = int(input().strip())
times = []
for i in range(num_rooms):
    times.append(list(map(int, input().strip().split())) + [i])


def approach1():
    arr, res = [], [0] * len(times)
    for [a, d, i] in times:
        arr.append((a, i + 1))
        arr.append((d + 1, -(i + 1)))

    cum_q, num_q = 0, -1
    arr.sort(key=lambda x: (x[0], x[1]))

    dq = deque()
    for t, i in arr:
        if i > 0:
            cum_q += 1
            res[i - 1] = dq.popleft() if dq else cum_q
            num_q = max(num_q, cum_q)
        else:
            cum_q -= 1
            dq.append(res[-i - 1])

    print(num_q)
    print(*res)


def approach2():
    pq, res = [], [0] * len(times)
    heapq.heapify(pq)

    for [arr, dep, i] in times:
        if pq and arr > pq[0][0]:
            t1, q = heapq.heappop(pq)
            heapq.heappush(pq, (dep, q))
            res[i] = q
            continue

        heapq.heappush(pq, (dep, len(pq) + 1))
        res[i] = len(pq)

    print(len(pq))
    print(*res)

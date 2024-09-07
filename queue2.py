import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    msg = input().strip().split()
    
    if msg[0] == "push":
        q.append(int(msg[1]))
    elif msg[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif msg[0] == "size":
        print(len(q))
    elif msg[0] == "empty":
        print(1 if not q else 0)
    elif msg[0] == "front":
        print(q[0] if q else -1)
    elif msg[0] == "back":
        print(q[-1] if q else -1)









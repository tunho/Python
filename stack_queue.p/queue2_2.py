import sys
import queue

input = sys.stdin.readline

n = int(input())
q = queue.Queue()

for _ in range(n):
    msg = input().strip().split()
    
    if msg[0] == "push":
        q.put(int(msg[1]))
    elif msg[0] == "pop":
        if q:
            print(q.get())
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


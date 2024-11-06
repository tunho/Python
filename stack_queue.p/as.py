import sys
from collections import deque




def bfs(mount,r_max_list):
    q = deque([(0,0)])
    r_max_list[0][0] = 0
    dx = [1,-1] # x변화량
    dy = [1,1]  # y변화량
    while q:
        sx, sy = q.popleft()
        # 산 범위확인
        for i in range(2):
            kx = sx + dx[i]
            ky = sy + dy[i]
            if kx < 0 or \
            kx > (2*n-ky) or \
            ky > 2 * n or \
            mount[kx][ky]: continue 
                
            if max(kx,r_max_list[sx][sy]) > r_max_list[kx][ky]:
                r_max_list[kx][ky] = max(kx,r_max_list[sx][sy])
                q.append((kx,ky))
input = sys.stdin.readline

n,m = map(int,input().split()) 

mount = [[False]*(2*n+1) for _ in range(n+1)] # 이등변삼각형 산 생성


for _ in range(m):
  y,x = map(int,input().split())
  mount[x][y] = True

max_high = [[-1]*(2*n+1) for _ in range(n+1)]

bfs(mount,max_high)

print(max_high[0][2*n])
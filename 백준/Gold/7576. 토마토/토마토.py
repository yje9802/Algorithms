from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 방향 이동

def bfs(dq):
    while dq:
        x, y = dq.popleft()
        for i in range(4): # 상하좌우
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                dq.append([nx, ny])

dq = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            dq.append([i, j]) # 토마토 위치를 queue에 append

bfs(dq)

res = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1) # 토마토가 모두 익지 않은 상황
            exit(0)
    res = max(res, max(i))

print(res - 1)

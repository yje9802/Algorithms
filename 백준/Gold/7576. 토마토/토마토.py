from sys import stdin
from collections import deque

# 입력 처리
M, N = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(dq):
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 격자 범위를 벗어나지 않으면서, 익지 않은 토마토인 경우
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                dq.append((nx, ny))

def get_ripe_date():
    days = 0
    for line in matrix:
        for tomato in line:
            if tomato == 0:
                return 0
        days = max(days, max(line))
    return days

dq = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            dq.append((i, j))

bfs(dq)

print(get_ripe_date() - 1)
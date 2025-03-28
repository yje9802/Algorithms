from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

maze = []
for _ in range(N):
    line = list(map(int, list(stdin.readline().strip())))
    maze.append(line)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if maze[ny][nx] == 1: # 이동 가능한 곳
                    maze[ny][nx] = maze[y][x] + 1
                    queue.append((nx, ny))

bfs(0, 0)

print(maze[N-1][M-1])
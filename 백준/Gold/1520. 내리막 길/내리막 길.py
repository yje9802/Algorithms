from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
                        
M, N = map(int, stdin.readline().split())

map_graph = [] # len(map_graph) == M / len(map_graph[i]) == N

for _ in range(M):
    line = list(map(int, stdin.readline().split()))
    map_graph.append(line)

# -1로 초기화된 DP 배열: 방문 여부 및 경로 수 저장용
dp = [[-1] * N for _ in range(M)]

# 상, 하, 좌, 우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_routes(y, x):
    if y == M - 1 and x == N - 1: # 도착지점 도달
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    # 현재 위치에서의 경로 수 초기화
    dp[y][x] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= ny < M and 0 <= nx < N:
            if map_graph[ny][nx] < map_graph[y][x]:
                dp[y][x] += find_routes(ny, nx)
    
    return dp[y][x]

print(find_routes(0, 0))
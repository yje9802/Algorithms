from sys import stdin

n = int(stdin.readline()) # 컴퓨터의 개수
c = int(stdin.readline()) # 연결 개수

connections = [[] for _ in range(n+1)] # 컴퓨터 연결 관계

for _ in range(c):
    a, b = map(int, stdin.readline().split())
    connections[a].append(b)
    connections[b].append(a)

visited = [False for _ in range(n+1)] # DFS 방문 여부
count = 0 # 방문한 컴퓨터 개수

def dfs(node):
    global visited, count
    
    visited[node] = True
    count += 1
    
    for n in connections[node]:
        if visited[n] is False:
            dfs(n)
            
dfs(1)
print(count - 1)
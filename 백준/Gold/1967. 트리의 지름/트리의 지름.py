import sys
from sys import stdin
sys.setrecursionlimit(10**6)

# 입력 처리
n = int(stdin.readline()) # 노드의 개수

# 노드가 1개일 땐 트리의 지름이 0
if n == 1:
    print(0)
    exit()

tree  = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, cost = map(int, stdin.readline().split())
    tree[a].append((b, cost))
    tree[b].append((a, cost))

# 가장 먼 노드 찾기
def dfs(node, dist):
    global max_dist, farthest_node
    
    if dist > max_dist:
        max_dist = dist
        farthest_node = node
    
    # 현재 노드와 연결된 모든 노드 탐색
    for next_node, cost in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, dist + cost) # 현재까지 이동한 거리(dist)에다가 현재 노드에서 다음 노드로 가는 비용(cost)을 더함

# 1번 노드에서 가장 먼 노드 찾기
visited = [False] * (n + 1)
max_dist, farthest_node = 0, 0
visited[1] = True
dfs(1, 0)

# 1번 노드와 가장 먼 노드에서 가장 먼 노드 찾기
visited = [False] * (n + 1)
max_dist = 0
visited[farthest_node] = True
dfs(farthest_node, 0)

print(max_dist)
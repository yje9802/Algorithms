from sys import stdin
import heapq

answer = 0

V, E = map(int, stdin.readline().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, stdin.readline().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False] * (V+1)
heap = [(0, 1)] # 1번 정점부터 시작

while heap:
    cost, start = heapq.heappop(heap)
    if visited[start]:
        continue
    
    visited[start] = True
    answer += cost
    
    for next_cost, next_v in graph[start]:
        if not visited[next_v]:
            heapq.heappush(heap, (next_cost, next_v))

print(answer)
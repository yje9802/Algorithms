from sys import stdin
import heapq

N = int(stdin.readline())
M = int(stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, stdin.readline().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

answer = 0

visited = [False] * (N+1)
heap = [(0, 1)] # 1버ㄴ 컴퓨터부터 시작

while heap:
    cost, start = heapq.heappop(heap)
    if visited[start]: # 이미 연결된 컴퓨터
        continue
    
    visited[start] = True
    answer += cost
    
    for nxt, nxt_cost in graph[start]:
        if not visited[nxt]:
            heapq.heappush(heap, (nxt_cost, nxt))

print(answer)
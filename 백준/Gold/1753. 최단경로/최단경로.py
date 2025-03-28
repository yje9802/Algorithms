from sys import stdin
import heapq

def dijkstra(start, graph, distance):
    hq = [] # 우선순위큐; 가장 짧은 거리를 먼저 처리하기 위해
    heapq.heappush(hq, (0, start))  # (거리, 노드)
    distance[start] = 0 # 시작 노드에서 시작 노드까지의 거리는 당연히 0
    
    while hq:
        dist, now = heapq.heappop(hq)
        
        if distance[now] < dist: # 이미 처리된 노드
            continue
        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]: # 기존보다 더 짧은 경로
                distance[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

INF = int(1e9)

graph = [[] for _ in range(V+1)] # 정점 정보
distance = [INF] * (V + 1) # 시작점에서 각 정점까지의 최단 거리 저장

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K, graph, distance)

for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])
from heapq import heappop, heappush

INF = int(1e9)
graph = [[]] # graph[i] : [[i번 노드와 연결된 노드, 비용], []]

def dijkstra(n, src, dest):
    global graph
    
    dist = [INF for _ in range(n+1)] # 시작 정점과의 거리를 저장하는 배열
    dist[src] = 0 # 시작 정점의 거리는 0
    pq = [[0, src]] # [시작 정점과의 거리, 노드]
    
    while pq:
        w, x = heappop(pq) # w는 거리, x는 노드
        
        if dist[x] < w:
            continue
        
        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            
            if ncost < dist[nx]:
                dist[nx] = ncost
                heappush(pq, [ncost, nx])
                
    return dist[dest]


def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n+1)]
    
    for fare in fares:
        src, dest, each_cost = fare
        graph[src].append([dest, each_cost])
        graph[dest].append([src, each_cost])
    
    answer = dijkstra(n, s, a) + dijkstra(n, s, b)
    for i in range(1, n+1):
        if s != i: # 출발점 아님
            answer = min(answer, dijkstra(n, s, i) + dijkstra(n, i, a) + dijkstra(n, i, b))
        
    return answer
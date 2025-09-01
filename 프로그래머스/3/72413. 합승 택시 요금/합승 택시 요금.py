from heapq import heappop, heappush

INF = int(1e9) # 무한대 설정
graph = [[]] # graph[i] : [[i번 노드와 연결된 노드, 비용], []]

def dijkstra(n, src):
    global graph
    
    dist = [INF for _ in range(n+1)] # src와의 거리를 저장하는 배열
    dist[src] = 0 # src와 src 사이의 거리는 0
    pq = [[0, src]] # pq[i] : [src와의 거리, 특정 노드]
    
    while pq:
        w, x = heappop(pq) # w는 src와의 최단 거리, x는 해당 노드
        
        if dist[x] < w:
            continue
        
        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            
            if ncost < dist[nx]:
                dist[nx] = ncost
                heappush(pq, [ncost, nx])
                
    return dist


def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n+1)]
    # graph 설정
    for fare in fares:
        src, dest, each_cost = fare
        graph[src].append([dest, each_cost])
        graph[dest].append([src, each_cost])
    
    answer = INF
    
    dist_S = dijkstra(n, s)
    dist_A = dijkstra(n, a)
    dist_B = dijkstra(n, b)
    
    for i in range(1, n+1):
        if dist_S[i] == INF or dist_A[i] == INF or dist_B[i] == INF:
            continue
        answer = min(answer, dist_S[i] + dist_A[i] + dist_B[i])
        
    return answer
from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)] # 연결관계 정리
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n+1) # 1번 노드로부터 떨어진 거리
    dist[1] = 0 # 1번 노드는 거리 0
    
    queue = deque([1])
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr]+1
                queue.append(neighbor)
    
    max_dist = max(dist)
    answer = dist.count(max_dist)
    
    return answer
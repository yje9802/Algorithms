from collections import defaultdict
import heapq

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    for a, b in tickets:
        heapq.heappush(graph[a], b)
    
    def dfs(curr):
        while graph[curr]:
            next = heapq.heappop(graph[curr])  # 가장 앞선 도착지 꺼냄
            dfs(next)
        answer.append(curr) # 경로가 역순으로 answer에 저장됨
    
    dfs("ICN")
    
    return answer[::-1]
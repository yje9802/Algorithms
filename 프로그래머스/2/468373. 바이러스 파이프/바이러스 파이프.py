from collections import deque

def solution(n, infection, edges, k):
    answer = 1
    
    infected = 1 << infection # 배양체 감염 여부
    
    graph = [[] for _ in range(n+1)]
    for a, b, pipe in edges:
        graph[a].append((b, pipe))
        graph[b].append((a, pipe))
    
    def spread(infected, pipe):
        q = deque()
        visited = [False] * (n+1)
        new_infected = infected
        
        # 현재 감염된 노드는 큐에 넣기
        for i in range(1, n+1):
            if new_infected & (1 << i):
                q.append(i)
                visited[i] = True
        
        while q:
            curr = q.popleft()
            for nxt, t in graph[curr]:
                if t != pipe: # 종류 다르면 안 함
                    continue
                if visited[nxt]:
                    continue
                
                visited[nxt] = True
                new_infected = new_infected | (1 << nxt)
                q.append(nxt)
        return new_infected
    
    def count_infected(infected): # 감염된 배양체 개수 구하는 메서드
        count = 0
        for i in range(1, n+1):
            if infected & (1 << i):
                count += 1
        return count
    
    def dfs(cnt, infected):
        result = count_infected(infected)
        if cnt == k:
            return result
        for pipe in (1, 2, 3):
            new_infected = spread(infected, pipe)
            result = max(result, dfs(cnt+1, new_infected))
        return result
    
    answer = dfs(0, infected)
    return answer
import heapq

def solution(n, costs):
    answer = 0
    
    edges = []
    for a, b, cost in costs:
        edges.append((cost, a, b))
    heapq.heapify(edges) # 비용 기준 간선 오름차순 정렬
    
    parent = [i for i in range(n)] # 유니온 파인드용 부모 배열
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False # 둘이 이미 같은 집합 내에 있었음
    
    while edges:
        cost, a, b = heapq.heappop(edges)
        if union(a, b): # 둘이 합쳐짐 -> 사이클을 생성하지 않아 선택 가능
            answer += cost
    
    return answer
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def solution(nodes, edges):
    answer = [0, 0]
    
    graph = defaultdict(set) # 노드 번호: set(연결된 노드1, ...)
    for edge in edges:
        a, b = edge
        graph[a].add(b)
        graph[b].add(a)
    
    # 각 서브 트리의 노드 종류 정리
    def calc_node_types(graph, visited, type_result, start):
        visited.add(start) # 시작하는 노드 방문 처리

        # 노드 종류 판단
        if (start % 2 == 1) and (len(graph[start]) % 2 == 1): # 홀수 노드
            type_result[0] += 1
        elif (start % 2 == 0) and (len(graph[start]) % 2 == 0): # 짝수 노드
            type_result[1] += 1
        elif (start % 2 == 1) and (len(graph[start]) % 2 == 0): # 역홀수 노드
            type_result[2] += 1
        elif (start % 2 == 0) and (len(graph[start]) % 2 == 1): # 역짝수 노드
            type_result[3] += 1

        for node in graph[start]:
            if node not in visited:
                calc_node_types(graph, visited, type_result, node)

        return
    
    visited = set()
    for node in nodes:
        if node not in visited:
            visited.add(node)
            node_types = [0, 0, 0, 0] # 홀수 노드, 짝수 노드, 역홀수 노드, 역짝수 노드
            calc_node_types(graph, visited, node_types, node)
            
            if node_types[0] + node_types[1] == 1:
                # (서브) 트리에서 홀수 or 짝수 노드가 하나 밖에 없기 때문에 홀짝 트리로 만들 수 있음
                answer[0] += 1
            if node_types[2] + node_types[3] == 1:
                answer[1] += 1
    
    return answer
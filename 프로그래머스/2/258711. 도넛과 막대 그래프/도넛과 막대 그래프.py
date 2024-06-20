def solution(edges):
    answer = [0, 0, 0, 0]
    
    nodes = {} # 정점 번호: [정점에서 나간 간선 수, 정점으로 들어온 간선 수]
    
    for edge in edges:
        a, b = edge
        # 나가는 간선 
        if not nodes.get(a):
            nodes[a] = [1, 0]
        else:
            nodes[a][0] += 1
        # 들어온 간선
        if not nodes.get(b):
            nodes[b] = [0, 1]
        else:
            nodes[b][1] += 1
    
    for key, values in nodes.items():
        outside, inside = values
        
        if outside >= 2 and inside == 0: # 생성한 정점
            answer[0] = key
        elif outside == 0 and inside > 0: # 막대 그래프
            answer[2] += 1
        elif outside >= 2 and inside >= 2: # 8자 그래프
            answer[3] += 1
        
    answer[1] = nodes[answer[0]][0] - answer[2] - answer[3]
    
    return answer
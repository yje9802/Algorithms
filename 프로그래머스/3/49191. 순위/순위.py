def solution(n, results):
    answer = 0
    
    # 0은 승패모름, 1은 이김, -1은 짐
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for winner, loser in results:
        graph[winner][loser] = 1
        graph[loser][winner] = -1
        
    for k in range(1, n+1): # 경유 노드
        for i in range(1, n+1): # 출발 노드
            for j in range(1, n+1): # 도착 노드
                if graph[i][k] == 1 and graph[k][j] == 1: # i가 k를 이기고 k가 j를 이겼다면
                    graph[i][j] = 1 # i가 j를 이김
                    graph[j][i] = -1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    
    for i in range(1, n+1):
        count = 0 # 승패를 확실하게 알 수 있는 경우의 개수
        for j in range(1, n+1):
            if graph[i][j] != 0:
                count += 1
        if count == n-1: # 자기 자신을 제외한 모든 선수와 승패를 낸 경우 -> 순위 확정 가능
            answer += 1
        
    return answer
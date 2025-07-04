from collections import defaultdict

def solution(n, results):
    answer = 0
    
    win_graph = defaultdict(list) # 자신이 이긴 선수 리스트
    lose_graph = defaultdict(list) # 자신에게 이긴 선수 리스트
    
    for winner, loser in results:
        win_graph[winner].append(loser)
        lose_graph[loser].append(winner)
    
    def dfs(graph, start, visited): # start는 승패를 파악하고자 하는 선수
        for player in graph[start]:
            if player not in visited:
                visited.add(player)
                dfs(graph, player, visited)
    
    for player in range(1, n+1):
        win_set = set()
        lose_set = set()
        
        dfs(win_graph, player, win_set) # player가 이긴 선수들
        dfs(lose_graph, player, lose_set) # player가 진 선수들
        
        if len(win_set) + len(lose_set) == n - 1:
            answer += 1
    
    return answer
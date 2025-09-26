def solution(k, dungeons):
    answer = 0
    
    n = len(dungeons)
    visited = [False] * n
    
    def dfs(curr_hp, cnt):
        max_cnt = cnt
        
        for i in range(n):
            if not visited[i] and curr_hp >= dungeons[i][0]:
                visited[i] = True
                max_cnt = max(max_cnt, dfs(curr_hp - dungeons[i][1], cnt+1))
                visited[i] = False # 백트래킹
        return max_cnt
    answer = dfs(k, 0)
    return answer
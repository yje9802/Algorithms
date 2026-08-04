def solution(board, skill):
    answer = 0
    
    n = len(board) # 세로 크기
    m = len(board[0]) # 가로 크기
    
    prefix = [[0] * (m+1) for _ in range(n+1)] # 누적합 배열
    
    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1: # 공격
            value = -degree
        else:
            value = degree
        # 누적합 배열 채우기
        prefix[r1][c1] += value
        prefix[r1][c2+1] -= value
        prefix[r2+1][c1] -= value
        prefix[r2+1][c2+1] += value
    
    # 가로 누적합
    for i in range(n):
        for j in range(1, m):
            prefix[i][j] += prefix[i][j-1]
    # 세로 누적합
    for j in range(m):
        for i in range(1, n):
            prefix[i][j] += prefix[i-1][j]
    
    # 최종적으로 내구도가 1인 건물의 개수 계산
    for r in range(n):
        for c in range(m):
            if board[r][c] + prefix[r][c] >= 1:
                answer += 1
    
    return answer
def solution(board, h, w):
    answer = 0
    n, m = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    color = board[h][w]
    for d in directions:
        nh, nw = h + d[0], w + d[1]
        if 0 <= nh < n and 0 <= nw < m:
            if board[nh][nw] == color:
                answer += 1
    return answer
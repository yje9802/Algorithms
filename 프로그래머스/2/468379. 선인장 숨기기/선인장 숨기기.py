from collections import deque

def solution(m, n, h, w, drops):
    answer = []
    INF = len(drops) + 1 # 비가 오지 않은 구역 표시
    
    land = [[INF] * n for _ in range(m)]
    for i, (x, y) in enumerate(drops):
        land[x][y] = i + 1
    
    # 동일한 구역에서 비맞은 건지, 다른 뒤쪽 구역에서 비 맞은 건지
    # 선인장 구역의 왼쪽 상단 꼭짓점, 오른쪽 하단 꼭짓점
    # (0, 0)이랑 (h-1, w-1)부터 시작 -> 칸 경계에 닿으면 한 칸 아래로 (1, 0) (h, w-1)
    # 오른쪽 하단 꼭짓점이 아래 경계랑 왼쪽 경계에 닿으면 종료
    
    dq = deque() # (x, y, 빗방울이 떨어진 순서)
    
    def sliding_window(arr, k):
        dq = deque() # 인덱스만 저장
        result = []
        
        for i, val in enumerate(arr):
            # 현재 값보다 큰 값들은 뒤에서 제거
            while dq and arr[dq[-1]] >= val:
                dq.pop()
            dq.append(i)

            # 윈도우 범위 벗어난 인덱스 제거
            if dq[0] <= i - k:
                dq.popleft()

            # 길이 k짜리 윈도우가 완성되면 최소값 기록
            if i >= k - 1:
                result.append(arr[dq[0]])
                
        return result
    
    row_min = [sliding_window(land[r], w) for r in range(m)]
    cols = n - w + 1
    
    best_val = -1
    best_r, best_c = 0, 0
    
    for c in range(cols):
        col = [row_min[r][c] for r in range(m)]
        col_min = sliding_window(col, h)

        for r in range(len(col_min)):
            val = col_min[r]
            if val > best_val or (val == best_val and (r < best_r or (r == best_r and c < best_c))):
                best_val = val
                best_r, best_c = r, c

    answer = [best_r, best_c]
    return answer
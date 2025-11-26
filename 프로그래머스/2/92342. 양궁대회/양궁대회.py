def solution(n, info):
    answer = [-1]
    max_diff = 0
    
    def dfs(idx, remain, arr): # 점수 인덱스, 남은 화살 개수, 현재 점수 배열
        nonlocal answer, max_diff
        
        # 종료 과정
        if idx == 11:
            if remain > 0: # 남은 화살이 있다면
                arr[10] += remain # 남은 화살은 0점에
            
            # 점수 계산
            ry = ap = 0
            for i in range(11):
                if info[i] == 0 and arr[i] == 0:
                    continue
                elif info[i] < arr[i]: # 라이언이 점수 가져감
                    ry += 10 - i
                else:
                    ap += 10 - i
            
            diff = ry - ap
            if diff <= 0:
                if remain > 0:
                    arr[10] -= remain
                return
            
            if diff > max_diff:
                max_diff = diff
                answer = arr[:]
            elif diff == max_diff:
                if arr[::-1] > answer[::-1]:
                    answer = arr[:]
            
            if remain > 0:
                arr[10] -= remain
            return
        
        need = info[idx] + 1 # 이기기 위해 라이언이 맞춰야 하는 최소 화살 개수
        if need <= remain:
            arr[idx] = need
            dfs(idx + 1, remain - need, arr)
            arr[idx] = 0 # 백트래킹
        
        # 이번에는 화살을 맞추지 않고 다음 점수로 넘어감
        dfs(idx+1, remain, arr)
    
    dfs(0, n, [0] * 11)
    return answer
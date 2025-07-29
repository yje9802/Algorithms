import sys
sys.setrecursionlimit(10000)

def solution(arr):
    answer = -1
    
    nums, ops = [], [] # arr에서 숫자와 연산자 분리

    for ch in arr:
        if ch in '+-':
            ops.append(ch)
        else:
            nums.append(int(ch))
    
    n = len(nums) # 숫자의 개수
    max_dp = [[-float('inf')] * n for _ in range(n)] # (i, j) 범위 계산 최대값 dp 테이블
    min_dp = [[float('inf')] * n for _ in range(n)] # 계산 최솟값 dp 테이블
    
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]
        
    for length in range(2, n+1): # 구간 길이
        for i in range(0, n-length+1): # 시작 인덱스
            j = i + length - 1 # 끝 인덱스
            
            for k in range(i, j):
                op = ops[k] # 연산자는 nums[k]와 nums[k+1] 사이
                if op == '+':
                    max_val = max_dp[i][k] + max_dp[k+1][j]
                    min_val = min_dp[i][k] + min_dp[k+1][j]
                else: # op == '-'
                    max_val = max_dp[i][k] - min_dp[k+1][j]
                    min_val = min_dp[i][k] - max_dp[k+1][j]
                
                max_dp[i][j] = max(max_dp[i][j], max_val)
                min_dp[i][j] = min(min_dp[i][j], min_val)
    
    answer = max_dp[0][n-1]
    return answer
def solution(n, tops):
    MOD = 10007
    answer = 0
    
    not_right = [0] * n
    right = [0] * n
    
    not_right[0] = 3 if tops[0] == 1 else 2
    right[0] = 1
    
    for i in range(1, n):
        if tops[i] == 1: # 위에 삼각형 붙어있는 경우
            not_right[i] = (3 * not_right[i-1] + 2 * right[i-1]) % MOD
            right[i] = (not_right[i-1] + right[i-1]) % MOD
        else:
            not_right[i] = (2 * not_right[i-1] + right[i-1]) % MOD
            right[i] = (not_right[i-1] + right[i-1]) % MOD
    
    answer = (not_right[-1] + right[-1]) % MOD
    return answer
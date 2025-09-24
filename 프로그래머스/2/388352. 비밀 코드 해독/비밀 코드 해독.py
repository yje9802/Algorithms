def combinations(n, r): # 1부터 n까지의 정수 중 5개 뽑는 조합
    result = []
    comb = []
    
    def backtrack(start):
        if len(comb) == r: # r개만큼 뽑음
            result.append(comb[:])
            return
        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1)
            comb.pop()
    
    backtrack(1) # 1부터 뽑기 시작
    return result

def solution(n, q, ans):
    answer = 0
    
    q_sets = [set(arr) for arr in q] # 미리 q를 set 리스트로 바꿔두면 교집합 계산 빠름
    
    combs = combinations(n, 5)
    for comb in combs:
        cnt = 0
        for i in range(len(q_sets)):
            if len(set(comb) & q_sets[i]) == ans[i]:
                cnt += 1
            else:
                break
        if cnt == len(q_sets):
            answer += 1
    
    return answer
def dfs(numbers, target, curr, idx):
    answer = 0
    
    if idx == len(numbers):
        if curr == target:
            answer += 1
        return answer
    
    answer += dfs(numbers, target, curr + numbers[idx], idx+1)
    answer += dfs(numbers, target, curr - numbers[idx], idx+1)
    return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer
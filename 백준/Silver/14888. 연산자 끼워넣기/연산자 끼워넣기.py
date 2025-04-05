from sys import stdin
from itertools import permutations

N = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))
ops = list(map(int, stdin.readline().split())) # +, -, *, // 개수

max_result = -float('inf') # 연산 최댓값
min_result = float('inf') # 연산 최솟값

def dfs(cnt, curr_result, plus, minus, multiply, divide):
    global max_result, min_result
    
    # 마지막 숫자까지 연산 완료
    if cnt == N:
        max_result = max(max_result, curr_result)
        min_result = min(min_result, curr_result)
        return
    
    if plus:
        dfs(cnt+1, curr_result + nums[cnt], plus-1, minus, multiply, divide)
    if minus:
        dfs(cnt+1, curr_result - nums[cnt], plus, minus-1, multiply, divide)
    if multiply:
        dfs(cnt+1, curr_result * nums[cnt], plus, minus, multiply-1, divide)
    if divide:
        if curr_result < 0:
            dfs(cnt+1, -(-curr_result // nums[cnt]), plus, minus, multiply, divide-1)
        else:
            dfs(cnt+1, curr_result // nums[cnt], plus, minus, multiply, divide-1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_result)
print(min_result)
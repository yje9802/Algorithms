from itertools import combinations

def get_sums(dices):
    # 주사위 여러 개가 주어졌을 때, 각 주사위에서 하나씩 눈을 골라 나올 수 있는 '모든 합'을 구한다.
    sums = []
    
    def dfs(idx, curr_sum):
        if idx == len(dices):
            sums.append(curr_sum)
            return
        for face in dices[idx]:
            dfs(idx+1, curr_sum + face)
    
    dfs(0, 0)
    sums.sort()
    return sums

def find_lower_cnt(arr, target):
    # arr에서 target보다 작은 값의 개수를 반환
    # arr에 target이 추가된 후 arr를 정렬했을 때 target의 인덱스가 된다.
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def solution(dice):
    answer = []
    
    n = len(dice) # 주사위의 개수
    max_win = -1 # 가장 높은 승리 횟수
    
    for comb in combinations(range(n), n//2):
        # comb는 A가 가져가는 주사위 번호
        A = [dice[i] for i in comb]
        B = [dice[i] for i in range(n) if i not in comb]
        
        A_sums = get_sums(A)
        B_sums = get_sums(B)
        
        win_cases = 0
        for a in A_sums:
            # B의 합 중에서 a보다 작은 값 개수 세기
            win_cases += find_lower_cnt(B_sums, a)
        
        if win_cases > max_win: # 승리할 확률이 가장 높은 주사위 조합 갱신
            max_win = win_cases
            answer = comb
        
    return [i+1 for i in answer]
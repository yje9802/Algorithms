def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right
    
    def can_finish(level):
        total = times[0] # 첫번째 퍼즐은 항상 한번에 풀 수 있음
        if total > limit:
            return False
        
        n = len(diffs)
        for i in range(1, n):
            k = max(0, diffs[i] - level)
            total += times[i] + (times[i-1] + times[i]) * k
            if total > limit:
                return False
        return True
        
    while left <= right:
        mid = (left + right) // 2
        if can_finish(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer
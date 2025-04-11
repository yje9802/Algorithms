def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    
    left = 0
    right = distance
    
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        left_stone = 0 # 거리를 구할 때 왼편의 돌
        
        for rock in rocks:
            dist = rock - left_stone
            if dist < mid:
                removed += 1
                if removed > n:
                    break
            else:
                left_stone = rock
        
        if removed > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer
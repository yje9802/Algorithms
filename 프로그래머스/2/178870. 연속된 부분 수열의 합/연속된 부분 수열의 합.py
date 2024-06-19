def solution(sequence, k):
    answer = [0, len(sequence)-1]
    
    start, end = 0, 0
    curr = sequence[0] # 현재 부분 수열의 합
    
    while start <= end:
        if curr == k:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            curr -= sequence[start]
            start += 1
        elif curr < k:
            end += 1
            if end == len(sequence): 
                break
            curr += sequence[end]
        elif curr > k:
            curr -= sequence[start]
            start += 1
    
    return answer
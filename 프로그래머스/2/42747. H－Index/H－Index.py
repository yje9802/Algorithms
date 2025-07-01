def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for num, citation in enumerate(citations, start=1):
        if citation >= num:
            answer = num
    
    return answer
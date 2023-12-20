def solution(s, skip, index):
    answer = ''
    not_skip = [chr(k) for k in range(97,123) if chr(k) not in skip]
    for i in s:
        cnt = 0
        start = not_skip.index(i)
        while cnt < index:
            if start + 1 == len(not_skip):
                start = -1
            cnt += 1
            start += 1
        answer += not_skip[start]
    
    return answer
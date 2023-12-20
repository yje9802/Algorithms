def solution(s, skip, index):
    answer = ''
    not_skip = [chr(k) for k in range(97, 123) if chr(k) not in skip]
    for i in s:
        found = (not_skip.index(i) + index) % len(not_skip)
        answer += not_skip[found]
    
    return answer
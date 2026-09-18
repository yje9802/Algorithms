from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    sizes = Counter(tangerine)
    for size, cnt in sizes.most_common():
        answer += 1
        k = k - cnt
        if k <= 0:
            break
    return answer
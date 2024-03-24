def solution(x):
    answer = False
    
    add = sum([int(n) for n in str(x)])
    if x % add == 0:
        answer = True
    return answer
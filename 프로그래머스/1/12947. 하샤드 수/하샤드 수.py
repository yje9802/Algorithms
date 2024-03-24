def solution(x):
    answer = False
    
    # add = sum([int(n) for n in str(x)])
    add = sum(map(int, list(str(x))))
    if x % add == 0:
        answer = True
    return answer
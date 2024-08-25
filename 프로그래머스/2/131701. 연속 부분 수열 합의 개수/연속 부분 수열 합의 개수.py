def solution(elements):
    answer = 0
    end = len(elements)
    
    i = 1
    sums = []
    while i < end:
        temp = elements[:i]
        sums.append(sum(temp))
        for j in range(1, end):
            idx = (j + i - 1) % end
            temp = temp[1:]
            temp.append(elements[idx])
            sums.append(sum(temp))
        i += 1
    
    sums.append(sum(elements))
    answer = len(set(sums))
        
    return answer
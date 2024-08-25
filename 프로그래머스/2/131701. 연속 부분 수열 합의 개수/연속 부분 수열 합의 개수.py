def solution(elements):
    end = len(elements)
    sums = []
    for i in range(end):
        temp = elements[:i+1]
        sums.append(sum(temp))
        for j in range(1, end):
            idx = (j + i) % end
            temp = temp[1:]
            temp.append(elements[idx])
            sums.append(sum(temp))
    
    sums.append(sum(elements))
    answer = len(set(sums))
        
    return answer
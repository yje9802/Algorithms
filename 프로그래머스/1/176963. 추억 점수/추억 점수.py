def solution(name, yearning, photo):
    answer = []
    
    scores = dict()
    for i in range(len(name)):
        scores[name[i]] = yearning[i]
    
    for ph in photo:
        total = 0
        for nm in ph:
            if nm not in scores.keys():
                continue
            else:
                total += scores[nm]
        answer.append(total)
        
    return answer
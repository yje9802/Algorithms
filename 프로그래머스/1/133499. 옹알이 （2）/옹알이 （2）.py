def solution(babbling):
    answer = 0
    four = ["aya", "ye", "woo", "ma"] # 할 수 있는 발음
    
    for word in babbling:
        for one in four:
            if one + one in word: # "연속해서 같은 발음을 하는 것을 어려워합니다.""
                continue
            else:
                word = word.replace(one, " ")
            if word.isspace(): # 발음할 수 없는 발음이 없다.
                answer += 1
                break
        
    return answer
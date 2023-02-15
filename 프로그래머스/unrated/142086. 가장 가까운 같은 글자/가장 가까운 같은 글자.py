def solution(s):
    answer = []
    chars = {}
    for i in range(len(s)):
        if s[i] in chars:
            answer.append(i - chars[s[i]])
        else:
            answer.append(-1)
        chars[s[i]] = i
    
    return answer
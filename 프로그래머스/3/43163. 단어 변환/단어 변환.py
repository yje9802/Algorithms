from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    dq = deque()
    dq.append((begin, 0)) # (시작 단어, 현재 단계)

    while dq:
        curr, step = dq.popleft()
        if curr == target:
            return step
        for word in words:
            diff_char = 0 # curr와 word 중 알파벳이 다른 부분의 수
            for i in range(len(word)):
                if curr[i] != word[i]:
                    diff_char += 1
            if diff_char == 1:
                dq.append((word, step+1))
    
    return answer
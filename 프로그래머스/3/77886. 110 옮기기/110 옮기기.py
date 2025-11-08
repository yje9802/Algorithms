from collections import deque

def solution(s):
    answer = []
    
    for x in s:
        cnt = 0
        dq = deque([])
        i = 0
        while i < len(x):
            dq.append(x[i])
            
            if len(dq) >= 3:
                temp = deque([])
                for _ in range(3):
                    ch = dq.pop()
                    temp.appendleft(ch)
                if ''.join(temp) == "110":
                    cnt += 1
                else:
                    dq.extend(temp)
            i += 1
        
        # x 새로 만들기
        rest = ''.join(dq)
        insert_pos = rest.rfind('0')  # 마지막 0의 위치

        if insert_pos == -1:  # 0이 없는 경우
            new_x = '110' * cnt + rest
        else:
            new_x = rest[:insert_pos+1] + '110' * cnt + rest[insert_pos+1:]
        
        answer.append(new_x)

    return answer
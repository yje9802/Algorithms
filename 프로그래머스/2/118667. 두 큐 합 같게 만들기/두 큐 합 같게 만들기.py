from collections import deque

def solution(queue1, queue2):
    dq1, dq2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(dq1), sum(dq2)
    
    for i in range(300000):
        if sum1 == sum2:
            return i
        elif sum1 > sum2:
            num = dq1.popleft()
            dq2.append(num)
            sum1 -= num
            sum2 += num
        else: # sum2가 sum1보다 클 때
            num = dq2.popleft()
            dq1.append(num)
            sum2 -= num
            sum1 += num
        
    return -1
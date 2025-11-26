def solution(s):
    answer = []
    
    cnt = 0 # 변환 횟수
    deleted = 0 # 제거된 0의 개수
    
    while True:
        if s == "1":
            break
        cnt += 1
        original = len(s)
        s = s.replace("0", "")
        deleted += original - len(s)
        s = str(bin(len(s))[2:])
    
    answer.append(cnt)
    answer.append(deleted)
    return answer
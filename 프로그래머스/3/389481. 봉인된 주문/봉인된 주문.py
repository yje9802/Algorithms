def solution(n, bans):
    answer = ''
    
    # 문자열 s의 순서 번호 반환
    def str_to_num(s):
        num = 0
        for ch in s:
            num = num * 26 + (ord(ch) - ord('a') + 1)
        return num
        
    # 순서 번호 num을 문자열로 변환
    def num_to_str(num):
        result = []
        while num > 0:
            num -= 1
            result.append(chr(ord('a') + (num % 26)))
            num //= 26
        return ''.join(reversed(result))
    
    banned_idx = sorted(str_to_num(b) for b in bans) # bans 원소를 순서 번호로 변환
    
    cnt = 0
    for ban in banned_idx:
        if ban - cnt <= n:
            cnt += 1
        else:
            break
    
    answer = num_to_str(n + cnt)
    
    return answer
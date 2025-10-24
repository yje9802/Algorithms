def solution(expressions):
    answer = []
    
    def is_valid_base(base, num_str):
        # num_str가 주어진 진법(base)에서 표현 가능한 숫자인지 확인
        return all(int(s) < base for s in num_str)
    
    def convert_base(base, num_str):
        # base 진법으로 변환
        return int(num_str, base)
    
    def calculate(a, op, b):
        if op == "+":
            return a + b
        return a - b
    
    max_base = 1 # 가능한 최소 진법
    for exp in expressions:
        for ch in exp:
            if ch.isdigit(): # 숫자면
                max_base = max(max_base, int(ch) + 1)
    
    possible_bases = set(range(max_base, 10)) # 가능한 진법 후보
    
    for exp in expressions:
        a, op, b, _, c = exp.split(" ")
        
        if c != "X": # 지워지지 않은 수식
            valid_bases = set() # 가능한 진법
            for base in possible_bases:
                if not (is_valid_base(base, a) and is_valid_base(base, b) and is_valid_base(base, c)): # base 진법으로는 불가능 -> 넘어감
                    continue
                
                # base 진법으로 변환
                new_a, new_b, new_c = convert_base(base, a), convert_base(base, b), convert_base(base, c)
                
                if calculate(new_a, op, new_b) == new_c: # base 진법으로 계산 가능하면 후보에 추가
                    valid_bases.add(base)
            possible_bases = possible_bases & valid_bases # 가능한 진법 후보 교집합
    
    for exp in expressions:
        a, op, b, _, c = exp.split()
        if c != 'X':
            continue
        
        results = set()
        for base in possible_bases:
            if not (is_valid_base(base, a) and is_valid_base(base, b)):
                continue
            
            new_a, new_b = convert_base(base, a), convert_base(base, b)
            cal_result = calculate(new_a, op, new_b) # 연산 결과
            
            if cal_result < 0: # 연산 결과가 음수가 될 수는 없음
                continue
            
            # 현재 cal_result은 10진수 결과이기 때문에 base 진수로 변환해줘야 함
            temp = ''
            if cal_result == 0:
                temp = '0'
            else:
                n = cal_result
                while n > 0:
                    temp = str(n % base) + temp
                    n //= base
            results.add(temp)
        
        if len(results) == 1:
            answer.append(exp.replace('X', results.pop()))
        else:
            answer.append(exp.replace('X', '?'))
    
    return answer
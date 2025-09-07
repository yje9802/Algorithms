from collections import defaultdict

def solution(orders, course):
    answer = []
    
    max_course_len = max(course) # 코스요리 구성하는 메뉴 개수가 최대인 경우
    course_freq = defaultdict(dict) # 코스 메뉴 구성 별 주문 횟수
    
    # target: dfs 조회 대상 문자열, start: 시작 인덱스, path: 현재까지 선택한 조합[]
    def dfs(target, start, path):
        L = len(path) # 현재까지 선택한 조합의 길이
        if L in course:
            p = ''.join(path)
            course_freq[L][p] = course_freq[L].get(p, 0) + 1 # 길이가 L인 메뉴 구성 p 주문 횟수 + 1
        if L == max_course_len: # 더이상 긴 메뉴 구성을 구할 필요 X
            return
        for i in range(start, len(target)):
            path.append(target[i])
            dfs(target, i+1, path)
            path.pop() # 백트래킹
    
    for order in orders:
        target = sorted(order)
        dfs(target, 0, []) # 각 주문 별 조합 dfs
    
    for c in course:
        if not course_freq[c]: # 한번도 c 길이의 메뉴 구성이 주문된 적 없음
            continue
        
        max_cnt = 0 # 각 길이의 메뉴 구성 중에 가장 많이 주문된 횟수
        for comb, cnt in course_freq[c].items():
            if cnt >= 2 and cnt > max_cnt:
                max_cnt = cnt
        if max_cnt >= 2:
            for comb, cnt in course_freq[c].items():
                if cnt == max_cnt:
                    answer.append(comb)
        
    return sorted(answer)
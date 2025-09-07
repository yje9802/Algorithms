from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for course_len in course:
        order_combs = [] # 메뉴 구성이 course_len 개인 조합 목록
        for order in orders: # 각 주문 별로 course_len 크기의 조합 계산
            order_combs += combinations(sorted(order), course_len)
        most_ordered = Counter(order_combs).most_common()
        answer += [comb for comb, cnt in most_ordered if cnt > 1 and cnt == most_ordered[0][1]]
    return [''.join(s) for s in sorted(answer)]
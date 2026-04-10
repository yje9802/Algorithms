def solution(dist_limit, split_limit):
    answer = 1 # 최소 1개는 무조건 나옴
    
    def simulate(dist_limit, two_cnt, three_cnt):
        leaf = 1
        split_left = dist_limit
        
        for _ in range(two_cnt):
            if split_left >= leaf:
                split_left -= leaf
                leaf = leaf * 2
            else:
                return leaf + split_left
        
        for _ in range(three_cnt):
            if split_left >= leaf:
                split_left -= leaf
                leaf = leaf * 3
            else:
                return leaf + split_left * 2
        
        return leaf
    
    two_cnt = 0 # 자식 노드 2개인 걸 몇 번 쓸지
    
    while True:
        three_cnt = 0 # 자식 노드 3개인 걸 몇 번 쓸지
        while True:
            if (2 ** two_cnt) * (3 ** three_cnt) > split_limit: # 조건 위배
                break
            
            leaves = simulate(dist_limit, two_cnt, three_cnt) # 실제로 만들 수 있는 리프 수
            answer = max(answer, leaves)
            
            three_cnt += 1
        two_cnt += 1
        if 2 ** two_cnt > split_limit:
            break
    return answer
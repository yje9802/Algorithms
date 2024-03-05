def solution(numbers, hand):
    answer = ''
    l, r = "*", "#" # 왼손, 오른손 엄지 위치
    lefts = [1, 4, 7, "*"]
    rights = [3, 6, 9, "#"]
    middles = [2, 5, 8, 0]
    
    for n in numbers:
        if n in lefts:
            answer += "L"
            l = n
        elif n in rights:
            answer += "R"
            r = n
        else:
            m = middles.index(n)
            if l in lefts:
                idx_l = lefts.index(l)
                diff_l = abs(m - idx_l)
            else:
                idx_l = middles.index(l) 
                diff_l = abs(m - idx_l) - 1
            if r in rights:
                idx_r = rights.index(r)
                diff_r = abs(m - idx_r)
            else:
                idx_r = middles.index(r) 
                diff_r = abs(m - idx_r) - 1
            
            if diff_l < diff_r:
                answer += "L"
                l = n
            elif diff_l > diff_r:
                answer += "R"
                r = n
            else:
                if hand == "left":
                    answer += "L"
                    l = n
                else:
                    answer += "R"
                    r = n
            
    return answer
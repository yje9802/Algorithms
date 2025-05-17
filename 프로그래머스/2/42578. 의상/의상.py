from collections import defaultdict

def solution(clothes):
    answer = 1
    
    clothes_type = defaultdict(int) # 특정 종류에 해당 하는 의상의 개수가 중요, 어떤 의상이 있는 지가 아니라
    for cloth in clothes:
        _, ctype = cloth
        clothes_type[ctype] += 1
    
    for count in clothes_type.values():
        answer *= count + 1 # 해당 종류에서 어떤 의상을 고를지 + 아예 고르지 않을지
    
    answer = answer - 1 # 하루에 최소 한 개의 의상은 입는다는 전제 때문에 마지막에 모든 의상을 입지 않는 경우 1을 빼준다.
    
    return answer
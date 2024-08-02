from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    n = len(users)
    e_len = len(emoticons)
    
    percents = [40,30,20,10] # 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
    discount_group = product(percents, repeat=e_len) # 각 이모티콘별 가능한 모든 할인율 조합
    
    # discount_group 모든 조합 돌기
    for comb in discount_group: # 4*e_len 만큼 반복
        plus = 0
        profit = 0

        for user in users:
            emoticon_buy = 0 # 해당 유저의 이모티콘 구매 금액
            for i in range(e_len):
                if comb[i] >= user[0]: # 유저별 최소 할인율 확인
                    emoticon_buy += emoticons[i] * ((100 - comb[i]) / 100)
                    
            # 가격 이상의 돈을 이모티콘 구매에 사용한다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입
            if user[1] <= emoticon_buy:
                plus += 1
            else: # 이모티콘 플러스 X, 대신 이모티콘 판매액이 증가
                profit += emoticon_buy

        if answer[0] < plus:
            answer = [plus, int(profit)]
        elif answer[0] == plus:
            if answer[1] < profit:
                answer = [plus, int(profit)]
                
    return answer
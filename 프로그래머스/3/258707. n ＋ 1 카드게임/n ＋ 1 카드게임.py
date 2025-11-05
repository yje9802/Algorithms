def solution(coin, cards):
    answer = 1
    n = len(cards)
    
    mine = set(cards[:n//3]) # 내가 갖고 있는 카드
    temp = set() # 뽑았는데 일단 갖지 않은 카드
    
    i = n//3
    while i < n:
        a, b = cards[i], cards[i+1]
        xa, xb = n+1-a, n+1-b # a에 더해서 n+1을 만드는 수
        
        if coin > 0 and xa in mine:
            coin -= 1
            mine.add(a)
        else:
            temp.add(a)
            
        if coin > 0 and xb in mine:
            coin -= 1
            mine.add(b)
        else:
            temp.add(b)
        
        done = False # 다음으로 넘어갈 수 있는지 여부
        for card in mine:
            if n+1-card in mine:
                done = True
                mine.remove(card)
                mine.remove(n+1-card)
                answer += 1
                break
            elif n+1-card in temp and coin > 0:
                done = True
                mine.remove(card)
                temp.remove(n+1-card)
                coin -= 1
                answer += 1
                break
        
        if done is False and temp and coin >= 2:
            for card in temp:
                if n+1-card in temp:
                    done = True
                    temp.remove(card)
                    temp.remove(n+1-card)
                    coin -= 2
                    answer += 1
                    break
        
        if done is False:
            return answer    
        else:
            i += 2
        
    return answer
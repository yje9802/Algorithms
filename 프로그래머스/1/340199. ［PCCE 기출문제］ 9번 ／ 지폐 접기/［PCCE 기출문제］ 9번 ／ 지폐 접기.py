def solution(wallet, bill):
    answer = 0
    # 지페의 가장 작은 길이가 지갑의 가장 작은 길이보다 작거나 같아야 함
    # 지폐의 가장 긴 길이가 지갑의 가장 긴 길이보다 작거나 같아야 함
    
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        
    return answer
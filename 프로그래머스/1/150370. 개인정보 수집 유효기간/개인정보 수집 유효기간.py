def solution(today, terms, privacies):
    answer = []
    
    t_year, t_month, t_day = map(int, today.split("."))
    
    # terms_dict {약관 종류 : 유효기간}
    terms_dict = {}
    for i in range(len(terms)):
        term = terms[i].split(" ")
        terms_dict[term[0]] = term[1]
    
    # privacies 확인
    for i in range(len(privacies)):
        privacy = privacies[i].split(" ") # privacy [수집된 날짜, 약관 종류]
        limit = int(terms_dict[privacy[1]]) # privacy[1]: 약관 종류 # 유효기간
        year, month, day = map(int, privacy[0].split("."))
        
        month += limit
        day -= 1
        if day == 0:
            month -= 1
            day = 28
            
        while month > 12:
            year += 1
            month -= 12
            
        if t_year > year:
            answer.append(i+1)
        elif t_year == year:
            if t_month > month:
                answer.append(i+1)
            elif t_month == month:
                if t_day > day:
                    answer.append(i+1)
        
    return answer
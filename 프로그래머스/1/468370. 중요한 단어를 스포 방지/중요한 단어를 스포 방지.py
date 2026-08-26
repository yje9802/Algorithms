def solution(message, spoiler_ranges):
    answer = 0
    n = len(message)
    
    words = [] # message의 단어 목록
    start = 0
    for i in range(n + 1):
        if i == n or message[i] == ' ':
            words.append((message[start:i], start, i-1))
            start = i + 1
    
    not_spoiler = set() # 스포일러가 아닌 구간에서 등장한 단어(한 번도 스포일러랑 겹치지 않음)
    revealed_at = [[] for _ in range(len(spoiler_ranges))]
    
    for word, ws, we in words:
        last_spoiler = -1
        for i, (ss, se) in enumerate(spoiler_ranges):
            if ws <= se and ss <= we:
                last_spoiler = i
        if last_spoiler == -1:
            not_spoiler.add(word)
        else:
            revealed_at[last_spoiler].append(word)
    
    seen = set() # 이전에 공개된 스포일러 단어
    for words in revealed_at:
        for word in words:
            if word not in not_spoiler and word not in seen:
                answer += 1
            seen.add(word)
    
    return answer
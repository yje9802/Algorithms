def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    who_report = {id: [] for id in id_list}
    reported = {id: 0 for id in id_list}
    
    for s in report:
        s = s.split(" ")
        if s[1] not in who_report[s[0]]:
            who_report[s[0]].append(s[1])
            reported[s[1]] += 1
    
    blocked = []
    for key, value in reported.items():
        if value >= k:
            blocked.append(key)
    for key, value in who_report.items():
        key_idx = id_list.index(key)
        for b in blocked:
            if b in value:
                answer[key_idx] += 1
    
    return answer
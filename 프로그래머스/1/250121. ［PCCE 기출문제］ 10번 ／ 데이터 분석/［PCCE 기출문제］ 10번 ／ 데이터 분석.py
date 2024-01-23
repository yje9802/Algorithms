def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_d = {
        "code": 0, "date": 1, "maximum": 2, "remain": 3
    }
    
    loc = ext_d[ext]
    
    for d in data:
        if d[loc] < val_ext:
            answer.append(d)
    
    s_loc = ext_d[sort_by]
    
    answer.sort(key = lambda x: x[s_loc])
        
    return answer
def solution(data, col, row_begin, row_end):
    answer = 0
    
    # 정렬하기: col-1번 원소를 오름차순 정렬 -> 값이 같으면 0번 원소 기준으로 내림차순
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    # S_i 구하기
    for i in range(row_begin, row_end + 1):
        s_i = 0
        for value in data[i-1]:
            s_i += value % i
        answer ^= s_i

    return answer
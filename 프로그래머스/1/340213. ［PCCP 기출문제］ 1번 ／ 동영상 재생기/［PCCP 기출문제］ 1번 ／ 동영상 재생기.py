def to_seconds(time_str): # 초 단위로 변환
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)
    
    def skip_opening(time):
        if op_start <= time <= op_end:
            return op_end
        return time
    
    pos = skip_opening(pos)
    
    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        else:
            pos = min(video_len, pos + 10)
        pos = skip_opening(pos)
    
    minute, second = pos // 60, pos % 60
    answer = f"{minute:02}:{second:02}"
    return answer
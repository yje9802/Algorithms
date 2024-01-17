def solution(players, callings):
    dict = {player : idx for idx, player in enumerate(players)}
    
    for calling in callings:
        loc = dict[calling] # 호명된 선수의 players에서의 인덱스
        # 딕셔너리에서 인덱스 정보 업데이트
        dict[calling] -= 1
        dict[players[loc-1]] += 1
        # players에서 위치 업데이트
        players[loc] = players[loc-1]
        players[loc-1] = calling
    return players
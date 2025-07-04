def solution(name):
    answer = 0
    
    # 전체 상하 조작 횟수 구하기
    for char in name:
        cnt = min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        answer += cnt
    
    move = len(name) - 1 # 좌우 조작 최대 횟수
    for i in range(len(name)):
        next_i = i + 1
        
        # A가 연속되는 구간 계산
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        # i까지 이동한 거리, 맨 끝에서부터 다음 유효한 문자를 다시 가야 하는 거리, 그대로 왼쪽으로 갈지, 오른쪽으로 돌아갈지 더 짧은 거리 선택
        backward = i + (len(name) - next_i) + min(i, len(name)-next_i)
        move = min(move, backward)
    answer += move
    return answer
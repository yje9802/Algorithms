from collections import deque

def solution(storage, requests):
    answer = 0
    
    # 외부를 표현하기 위해 기존 storage 배열 상하좌우에 추가
    n = len(storage)
    m = len(storage[0])
    N = n + 2
    M = m + 2
    
    graph = [['0'] * M for _ in range(N)]
    for i in range(n):
        for j in range(m):
            graph[i+1][j+1] = storage[i][j]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 연결된 외부를 전부 '0'으로 바꾸는 함수
    def update_outside():
        visited = [[False] * M for _ in range(N)]
        dq = deque()
        
        # 가장 왼쪽 상단의 외부부터 시작
        dq.append((0, 0))
        visited[0][0] = True
        
        while dq:
            x, y = dq.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    # 만약 이 위치가 빈 공간 '0' 또는 표시된 외부 연결 가능한 공간 '1'로 표기되어 있다면
                    if graph[nx][ny] == '0':
                        visited[nx][ny] = True
                        dq.append((nx, ny)) # 여기와 연결된 다른 외부가 있는지 탐색
                    elif graph[nx][ny] == '1':
                        # 이 공간이 외부와 연결 가능하므로 이제 빈 공간으로 바꿔도 됨
                        graph[nx][ny] = '0'
                        dq.append((nx, ny))
                        visited[nx][ny] = True
        # 끝난 뒤 graph 내에는 외부와 연결된 공간이 모두 ‘0’이 된다.
    
    for req in requests:
        update_outside() # 일단 갱신 한번
        
        ch = req[0] # 꺼내고 싶은 컨테이너 종류
        
        if len(req) == 1: # 외부와 연결된 컨테이너만 꺼낼 수 있음
            to_remove = [] # 꺼낼 컨테이너 위치 저장
            for i in range(1, N-1):
                for j in range(1, M-1):
                    if graph[i][j] == ch:
                        for d in range(4): # 상하좌우 중 하나라도 외부이면 꺼내도 됨
                            ni = i + dx[d]
                            nj = j + dy[d]
                            if graph[ni][nj] == '0':
                                to_remove.append((i, j))
                                break
            # 한꺼번에 꺼내기
            # 이렇게 한번에 안 꺼내면 예시 1번의 세번째 케이스 같은 경우에 문제 생김
            for (i, j) in to_remove:
                graph[i][j] = '0'
            update_outside()
            
        elif len(req) == 2:
            for i in range(1, N-1):
                for j in range(1, M-1):
                    if graph[i][j] == ch:
                        graph[i][j] = '1'
            update_outside()
    
    # 남은 컨테이너 개수 세기
    for i in range(1, N-1):
        for j in range(1, M-1):
            if graph[i][j] != '0' and graph[i][j] != '1':
                answer += 1
    return answer
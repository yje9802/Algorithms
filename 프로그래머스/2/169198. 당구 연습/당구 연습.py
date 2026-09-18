def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        ballX, ballY = ball
        distances = [] # 굴러가는 거리
        
        # 왼쪽 벽으로 굴리기
        if not(startY == ballY and ballX < startX):
            d1 = (startX + ballX) ** 2 + (startY - ballY) ** 2
            distances.append(d1)
        # 오른쪽 벽으로 굴리기
        if not(startY == ballY and startX < ballX):
            d2 = (2 * m - startX - ballX) ** 2 + (startY - ballY) ** 2
            distances.append(d2)
        # 위쪽 벽으로 굴리기
        if not(startX == ballX and startY < ballY):
            d3 = (startX - ballX) ** 2 + (2 * n - startY - ballY) ** 2
            distances.append(d3)
        # 아래쪽 벽으로 굴리기
        if not(startX == ballX and ballY < startY):
            d4 = (startX - ballX) ** 2 + (startY + ballY) ** 2
            distances.append(d4)
        answer.append(min(distances))
        
    return answer
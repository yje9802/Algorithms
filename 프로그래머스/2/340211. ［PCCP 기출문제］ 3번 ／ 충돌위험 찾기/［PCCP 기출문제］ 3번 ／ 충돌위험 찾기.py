def move(x, y, to_x, to_y):
    if x > to_x:
        return (x-1, y)
    elif x < to_x:
        return (x+1, y)
    
    if y > to_y:
        return (x, y-1)
    elif y < to_y:
        return (x, y+1)
    
    return (x, y)

def solution(points, routes):
    answer = 0
    
    point_dict = dict() # 포인트 번호: [포인트 위치]
    for i in range(len(points)):
        point_dict[i+1] = points[i]
    
    robots = [] # (로봇의 x좌표, 로봇의 y좌표, [목표지점 반대로])
    for route in routes:
        start_x, start_y = point_dict[route[0]]
        robots.append((start_x, start_y, route[::-1]))
    
    while robots:
        tmp_robots = []
        robots_pos = dict()
        
        for robot in robots:
            x, y, route = robot
            # 로봇 충돌 계산을 위해 현재 위치의 로봇 count 추가
            if (x, y) in robots_pos:
                robots_pos[(x, y)] += 1
            else:
                robots_pos[(x, y)] = 1
            
            # 현재 위치가 목표에 도달한 경우, 목표 경로 제거
            if [x, y] == point_dict.get(route[-1]):
                route.pop()
            
            # 다음 경로가 남은 경우
            if route:
                to_x, to_y = point_dict.get(route[-1])
                x, y = move(x, y, to_x, to_y)
                tmp_robots.append((x, y, route))
        
        # 충돌 위험 계산
        answer += sum([1 if i >= 2 else 0 for i in robots_pos.values()])
        robots = tmp_robots
    
    return answer
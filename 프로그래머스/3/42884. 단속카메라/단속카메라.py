def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[1]) # 진출 시점으로 정렬
    
    camera = -30001 # 가장 최근 카메라 설치한 위치; 초기값은 카메라가 아직 설치되지 않았으므로 의미 없는 값
    for route in routes:
        if route[0] > camera: # 가장 가까운 카메라로 단속 불가 -> 진출 시점에 카메라 새로 설치
            camera = route[1]
            answer += 1
    
    return answer
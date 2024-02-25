def solution(park, routes):
    answer = [0, 0]
    ways = [r.split(" ") for r in routes]
    route = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}
    
    w = len(park[0])
    h = len(park)

    i, j = 0, 0
    while i < w and j < h:
        if park[i][j] == "S":
            answer = [i, j]
            break
        i += 1
        if i == w:
            i = 0
            j += 1
    
    for way in ways:
        x, y = answer[0], answer[1]
        d = way[0]
        n = int(way[1])
        
        for _ in range(n):
            x += route[d][0]
            y += route[d][1]
            
            if 0 <= x < h and 0 <= y < w and park[x][y] != "X":
                continue
            else:
                x, y = -1, -1
                break
        if x != -1 and y != -1:
            answer = [x, y]

    return answer
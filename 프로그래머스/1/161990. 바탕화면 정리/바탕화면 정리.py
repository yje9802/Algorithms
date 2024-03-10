def solution(wallpaper):
    h, w = len(wallpaper), len(wallpaper[0])
    lux, luy = -1, -1
    rdx, rdy = 0, 0
    for i in range(h):
        if "#" in wallpaper[i]:
            for j in range(w):
                if wallpaper[i][j] == "#":
                    if lux == -1:
                        lux = i
                        luy = j
                        rdx = i + 1
                        rdy = j + 1
                    else:
                        if j < luy:
                            luy = j
                        elif j >= rdy:
                            rdy = j+1
                        rdx = i + 1
    answer = [lux, luy, rdx, rdy]
        
    return answer
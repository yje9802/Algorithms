def solution(wallpaper):
    h, w = len(wallpaper), len(wallpaper[0])
    x, y = [], []
    
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                x.append(i)
                y.append(j)
    answer = [min(x), min(y), max(x)+1, max(y)+1]
    return answer
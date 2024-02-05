import sys
input = sys.stdin.readline

def solution(heights):
    result = 0
    N = len(heights)

    heights = heights + [0] # 마지막 부분까지 확인하기 위해 임의로 추가
    stack = [(0, heights[0])] # 만약 어떤 높이 h로 쭉 이어갈 수 있다면, 그 출발점이 되는 인덱스와 그 높이 h

    for i in range(1, N+1):
        start = i
        while stack and stack[-1][1] > heights[i]:
            start, s_heights = stack.pop()
            result = max(result, s_heights * (i - start))
        stack.append((start, heights[i]))

    return result

N = int(input())
heights = []
for _ in range(N):
    num = int(input())
    heights.append(num)
   
print(solution(heights))
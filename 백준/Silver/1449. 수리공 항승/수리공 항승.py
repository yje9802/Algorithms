from sys import stdin

N, L = map(int, stdin.readline().split())

leakage = list(map(int, stdin.readline().split()))
leakage.sort()

answer = 1

start = leakage[0] # 마지막으로 테이프 붙인 지점
for i in range(1, len(leakage)):
    if leakage[i] - start + 1 <= L:
        continue
    else:
        answer += 1
        start = leakage[i]

print(answer)
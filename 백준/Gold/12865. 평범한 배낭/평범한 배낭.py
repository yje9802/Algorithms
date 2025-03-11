from sys import stdin

N, K = map(int, stdin.readline().split())
items = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [0] * (K + 1)

# DP 수행
for weight, value in items:
    for w in range(K, weight - 1, -1): # 맨뒤부터
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[K])
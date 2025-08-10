from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

# 입력 처리
N = int(stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int, stdin.readline().split())))

INF = int(1e9)

def dfs(curr, bit):
    # 모든 도시를 방문 완료
    if bit == (1 << N) - 1:
        if graph[curr][0] != 0:
            # pre -> 0번 도시로 가는 비용 리턴
            return graph[curr][0]
        else:
            return INF
        
    if dp[curr][bit] != -1: # 이미 구한 적이 있음
        return dp[curr][bit]

    dp[curr][bit] = INF # 무의미한 값
    for i in range(N):
        # 아직 방문 안 한 도시가 있고 길이 있으면
        if not (bit & (1 << i)) and graph[curr][i] != 0:
            dp[curr][bit] = min(dp[curr][bit], dfs(i, bit | (1 << i)) + graph[curr][i])
    return dp[curr][bit]

dp = [[-1] * (1 << N) for _ in range(N)]
print(dfs(0, 1))
from sys import stdin
from collections import deque, defaultdict

N, M = map(int, stdin.readline().split()) # 과목의 수, 선수 조건의 수

subjects = defaultdict(list) # key 과목을 수강한 후에 수강 가능한 과목 리스트
n_pre = [0] * (N+1) # i번 과목을 듣기 위해 필요한 선수과목의 개수
semesters = [1] * (N+1) # i번 과목을 들을 수 있는 학기

for _ in range(M):
    first, second = map(int, stdin.readline().split())
    subjects[first].append(second)
    n_pre[second] += 1

queue = deque()

# 선수과목이 없는 과목부터 시작
for i in range(1, N+1):
    if n_pre[i] == 0: # 선수과목이 없는 과목
        queue.append(i)

while queue:
    curr = queue.popleft()
    
    for next_sub in subjects[curr]:
        n_pre[next_sub] -= 1 # 선수과목 하나 이수했으므로 빼줌
        semesters[next_sub] = max(semesters[next_sub], semesters[curr] + 1) # 여러 선수과목 중 가장 늦게 듣는 과목 + 1이 최소 수강 학기
        if n_pre[next_sub] == 0: # 선수과목을 전부 들은 경우
            queue.append(next_sub)

print(*semesters[1:])
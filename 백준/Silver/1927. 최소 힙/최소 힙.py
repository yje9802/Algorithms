from sys import stdin
import heapq

N = int(stdin.readline())

hq = [] # 우선순위 큐
for i in range(N):
	num = int(stdin.readline())
	if num == 0:
		if not hq:
			print(0)
		else:
			print(heapq.heappop(hq))
	else:
		heapq.heappush(hq, num)
from sys import stdin

word1, word2 = stdin.readline().strip(), stdin.readline().strip()
l1, l2 = len(word1), len(word2)
cache = [0 for _ in range(l2)] # word2에 대해 캐시 지정

for i in range(l1):
	cnt = 0 # 누적값을 저장할 변수
	for j in range(l2): # 비교 시작
		if cnt < cache[j]:
			cnt = cache[j]
		elif word1[i] == word2[j]:
			cache[j] = cnt + 1

print(max(cache))
from sys import stdin

n, m = map(int, stdin.readline().split())
operations = []
for _ in range(m):
    operations.append(list(map(int, stdin.readline().split())))
    
sets = [i for i in range(n+1)] # sets[i]는 i가 포함된 집합의 헤드를 가리킴; 초기에는 다 서로 다른 집합에 속해 있으므로 i가 자기 자신을 가리킴

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        sets[root_b] = root_a

def find(x):
    if sets[x] != x:
        sets[x] = find(sets[x])
    return sets[x]

for op, a, b in operations:
    if op == 0:
        union(a, b)
    elif op == 1:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            print("YES")
        else:
            print("NO")
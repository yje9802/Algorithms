from collections import deque
import math

def solution(players, m, k):
    answer = 0
    
    servers = deque([])
    
    for player in players:
        curr_servers = len(servers)
        for _ in range(curr_servers): # 이미 증설한 서버 운영 시간 감소
            server = servers.popleft()
            if server > 1:
                servers.append(server-1)
        
        needed = player // m
        if len(servers) < needed:
            add = needed - len(servers)
            answer += add
            for _ in range(add):
                servers.append(k)
    
    return answer
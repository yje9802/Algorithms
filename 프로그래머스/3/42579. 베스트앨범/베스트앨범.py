import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_count = {} # 장르명: 총 재생 횟수
    genre_plays = defaultdict(list) # 장르명: [(-재생 횟수, 고유번호), ...]
    for i in range(len(plays)):
        if genres[i] in genre_count:
            genre_count[genres[i]] += plays[i]
        else:
            genre_count[genres[i]] = plays[i]
        genre_plays[genres[i]].append((-plays[i], i))
    
    genre_count_order = []
    heapq.heapify(genre_count_order)
    for k, v in genre_count.items():
        counts = (-v, k)
        heapq.heappush(genre_count_order, counts)
    
    while genre_count_order:
        _, genre = heapq.heappop(genre_count_order)
        g_plays = genre_plays[genre]
        heapq.heapify(g_plays)
        for _ in range(2):
            if g_plays:
                _, play = heapq.heappop(g_plays)
                answer.append(play)
    
    return answer
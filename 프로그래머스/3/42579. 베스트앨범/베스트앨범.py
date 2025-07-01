import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_count = defaultdict(int) # 장르명: 총 재생 횟수
    genre_plays = defaultdict(list) # 장르명: [(-재생 횟수, 고유번호), ...]
    for i in range(len(plays)):
        genre_count[genres[i]] += plays[i]
        genre_plays[genres[i]].append((-plays[i], i))
    
    # 많이 재생된 순으로 장르 정렬
    genre_count_order = sorted(genre_count.items(), key=lambda x: -x[1])
    
    for genre, _ in genre_count_order:
        g_plays = genre_plays[genre]
        heapq.heapify(g_plays)
        for _ in range(2):
            if g_plays:
                _, idx = heapq.heappop(g_plays)
                answer.append(idx)
    
    return answer
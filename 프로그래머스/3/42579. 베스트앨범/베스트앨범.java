import java.util.*;

class Solution {
    static class Song {
        int idx;
        int play;

        Song(int idx, int play) {
            this.idx = idx;
            this.play = play;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        Map<String, Integer> genreCount = new HashMap<>(); // 장르: 총 재생 횟수
        Map<String, List<Song>> genrePlays = new HashMap<>(); // 장르: [Song(고유번호, 재생횟수), ...]
        
        for (int i = 0; i < plays.length; i++) {
            genreCount.put(genres[i], genreCount.getOrDefault(genres[i], 0) + plays[i]);
            genrePlays.computeIfAbsent(genres[i], k -> new ArrayList<>()).add(new Song(i, plays[i]));
        }
        
        // 속한 노래가 많이 재생된 장르 순으로 정렬
        List<String> sortedGenres = new ArrayList<>(genreCount.keySet());
        sortedGenres.sort((genre1, genre2) -> genreCount.get(genre2) - genreCount.get(genre1));
        
        for (String genre: sortedGenres) {
            List<Song> songs = genrePlays.get(genre);
            songs.sort((song1, song2) -> {
                if (song2.play != song1.play) return song2.play - song1.play; // 재생 수 내림차순
                return song1.idx - song2.idx; // 고유번호 오름차순
            });
            
            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                answer.add(songs.get(i).idx);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
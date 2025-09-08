import java.util.*;

class Solution {
    Map<Integer, Map<String, Integer>> courseFreq = new HashMap<>();
    Set<Integer> courseSet = new HashSet<>();
    int maxCourseLen;
    
    public String[] solution(String[] orders, int[] course) {
        String[] answer;
        
        for (int c: course) {
            courseSet.add(c);
            courseFreq.put(c, new HashMap<>());
            maxCourseLen = Math.max(maxCourseLen, c);
        }
        
        for (String order: orders) {
            char[] orderList = order.toCharArray();
            Arrays.sort(orderList); // 주문 메뉴 오름차순 정렬
            dfs(orderList, 0, new StringBuilder());
        }
        
        List<String> result = new ArrayList<>();
        for (int c: course) {
            Map<String, Integer> orderCombs = courseFreq.get(c);
            if (orderCombs.isEmpty()) continue; // 메뉴 개수가 c개를 충족하는 코스요리를 만들 수 없는 경우
            int mostOrdered = 0;
            for (int cnt: orderCombs.values()) if (cnt >= 2) mostOrdered = Math.max(mostOrdered, cnt);
            
            if (mostOrdered < 2) continue; // 조건 충족 미달
            
            for (Map.Entry<String, Integer> e: orderCombs.entrySet()) {
                if (e.getValue() == mostOrdered) {
                    result.add(e.getKey());
                }
            }
        }
        Collections.sort(result);
        answer = result.toArray(new String[0]);
        return answer;
    }
    
    private void dfs(char[] target, int start, StringBuilder path) {
        int L = path.length();
        
        if (courseSet.contains(L)) {
            courseFreq.get(L).merge(path.toString(), 1, Integer::sum);
        }
        
        if (L == maxCourseLen) return; // 탈출 조건
        
        for (int i = start; i < target.length; i++) {
            path.append(target[i]);
            dfs(target, i+1, path);
            path.deleteCharAt(path.length() - 1); // 백트래킹
        }
    }
}
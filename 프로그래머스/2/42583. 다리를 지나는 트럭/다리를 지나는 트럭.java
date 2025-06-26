import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> trucks = new LinkedList<>(
            Arrays.asList(Arrays.stream(truck_weights).boxed().toArray(Integer[]::new))
        ); // truck_weights를 Queue로 변환
        
        Queue<Integer> currBridge = new LinkedList<>(
            Collections.nCopies(bridge_length, 0)
        ); // bridge_length 만큼 0으로 초기화
        
        int currWeight = 0;
        
        while (!currBridge.isEmpty()) {
            answer++;
            currWeight -= currBridge.poll(); // 1초에 다리 한 칸 전진
            
            if (!trucks.isEmpty()) {
                int nextTruck = trucks.peek();
                if (currWeight + nextTruck <= weight) {
                    currBridge.offer(trucks.poll());
                    currWeight += nextTruck;
                } else {
                    currBridge.offer(0); // 다리에 트럭이 추가로 올라가지 못 함
                }
            }
        }
        
        return answer;
    }
}
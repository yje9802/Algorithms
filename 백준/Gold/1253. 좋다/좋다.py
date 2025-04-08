from sys import stdin

N = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))
nums.sort()

answer = 0

for i in range(N):
    target = nums[i]
    left = 0
    right = N-1
    
    while left < right:
        if nums[left] + nums[right] == target:
            if left != i and right != i:
                answer += 1
                break
            elif left == i:
                left += 1
            else:
                right -= 1
            
        elif nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1

print(answer)
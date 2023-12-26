def solution(numbers):
    answer = sum([i for i in range(0, 10)]) - sum(numbers)
    return answer
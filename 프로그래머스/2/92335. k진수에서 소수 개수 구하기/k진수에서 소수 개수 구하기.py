import math

def k_num(n, k): # k진수 변환
    if k == 10:
        return n
    result = ""
    while n > 0:
        result += str(n % k)
        n //= k
    return result[::-1]

def is_prime(n): # 소수 판별
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    kn = k_num(n, k)

    # 0이 들어가면 어차피 소수가 될 수 없다.
    kn_split = str(kn).split("0")
    for num in kn_split:
        if num and is_prime(int(num)):
            answer += 1
    return answer
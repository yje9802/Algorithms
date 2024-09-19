def gcd(a, b): # 두 수의 최대공약수 구하기
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def get_gcd(arr): # arr의 모든 원소에 대하여 최대공약수 구하기
    start_gcd = arr[0]
    for n in arr[1:]:
        start_gcd = gcd(start_gcd, n)
    return start_gcd

def solution(arrayA, arrayB): 
    gcd_a = get_gcd(arrayA) # arrayA의 최대공약수
    gcd_b = get_gcd(arrayB) # arrayB의 최대공약수
    
    for a in arrayA:
        if a % gcd_b == 0:
            gcd_b = 0
            break
    for b in arrayB:
        if b % gcd_a == 0:
            gcd_a = 0
            break
    
    answer = max(gcd_a, gcd_b)
    
    return answer
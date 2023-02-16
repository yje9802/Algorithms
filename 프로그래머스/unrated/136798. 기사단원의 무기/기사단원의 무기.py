def solution(number, limit, power):
    answer = 0

    for i in range(number):
        i += 1
        divisors = []
        for j in range(1, int(i**(1/2))+1):
            if (i % j == 0):
                divisors.append(j)
                if ((j ** 2) != i):
                    divisors.append(i // j)
        divisors.sort()
        if len(divisors) > limit:
            answer = answer + power
        else:
            answer = answer + len(divisors)
    
    return answer
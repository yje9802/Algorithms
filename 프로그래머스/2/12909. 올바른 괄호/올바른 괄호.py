def solution(s):
    list_s = list(s)

    if list_s[-1] == '(':
        return False

    stack = []
    
    while list_s:
        par = list_s.pop()
        if par == ')':
            stack.append(par)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
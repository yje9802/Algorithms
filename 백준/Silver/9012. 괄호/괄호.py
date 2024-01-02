T = int(input())

for i in range(T):
    stack = []
    s = input()
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: 
        if not stack: 
            print("YES")
        else: # 스택에 괄호가 남아있다면 NO이다.
            print("NO")
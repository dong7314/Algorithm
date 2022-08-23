isp = {'*' : 2, '+' : 1, '(' : 0}
icp = {'*' : 2, '+' : 1, '(' : 3}


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input())

    stack = []
    temp = []
    for i in range(N):
        if arr[i].isdecimal():
            temp.append(arr[i])
        elif arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
        elif icp[arr[i]] > isp[stack[-1]]:
            stack.append(arr[i])
        else:
            while icp[arr[i]] <= isp[stack[-1]]:
                temp.append(stack.pop())
            stack.append(arr[i])

    for i in range(len(temp)):
        if temp[i].isdecimal():
            stack.append(temp[i])
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if temp[i] == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)

    print(f'#{tc} {stack[0]}')


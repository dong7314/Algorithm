T = 10
for tc in range(1, T + 1):
    N = int(input())
    calculate = input()

    stack1 = []
    stack2 = []
    for ch in calculate:
        if len(stack2) != 0:
            if stack2[-1] == '*':
                num1 = int(stack1.pop())
                num2 = int(ch)
                stack1.append(num1 * num2)
                stack2.pop()
                continue

        if ch == '+' or ch == '*':
            stack2.append(ch)
        else:
            stack1.append(ch)

    while len(stack2):
        num1 = int(stack1.pop())
        num2 = int(stack1.pop())

        stack1.append(num1 + num2)
        stack2.pop()

    print(f'#{tc} {stack1[0]}')




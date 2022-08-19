T = int(input())
for tc in range(1, T + 1):
    stick = input()

    stack = []
    skip = 0
    for i in range(len(stick)):
        if skip == 1:
            skip = 0
            continue
        if stick[i] == '(' and stick[i + 1] == ')':
            stack.append('r')
            skip = 1
        else:
            stack.append(stick[i])

    cnt = 0
    total = 0
    while len(stack):
        iron = stack.pop()
        if iron == ')':
            cnt += 1
        elif iron == '(':
            cnt -= 1
            total += 1

        if len(stack) == 0:
            total += cnt

        if len(stack) != 0:
            if stack[-1] == 'r':
                total += cnt

    print(f'#{tc} {total}')

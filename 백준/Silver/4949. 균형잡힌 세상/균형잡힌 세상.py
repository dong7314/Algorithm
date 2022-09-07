def checking(arr):
    stack = []
    for ch in arr:
        if ch == '(':
            stack.append(ch)
        elif ch == '[':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0:
                return 'no'
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
        elif ch == ']':
            if len(stack) == 0:
                return 'no'
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 'no'

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

string = []
while True:
    st = input()
    if st == '.':
        break
    string.append(st)

for st in string:
    print(checking(st))
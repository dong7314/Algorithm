def postorder(node):
    if node <= N:
        if tree[node] in ['-', '+', '*', '/']:
            num1 = postorder(ch1[node])
            num2 = postorder(ch2[node])
            if tree[node] == '+':
                return num1 + num2
            elif tree[node] == '-':
                return num1 - num2
            elif tree[node] == '/':
                return num1 / num2
            elif tree[node] == '*':
                return num1 * num2
        else:
            return tree[node]
 
T = 10
for tc in range(1, T + 1):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        arr = input().split()
        if len(arr) == 4:
            tree[i] = arr[1]
            ch1[i] = int(arr[2])
            ch2[i] = int(arr[3])
        else:
            tree[i] = int(arr[1])
 
    print(f'#{tc} {int(postorder(1))}')
def preorder(node):
    if node == 0:
        return
    else:
        preorder(ch1[node])
        result.append(tree[node])
        preorder(ch2[node])

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
        elif len(arr) == 3:
            tree[i] = arr[1]
            ch1[i] = int(arr[2])
        else:
            tree[i] = arr[1]

    result = []
    preorder(1)
    result = ''.join(result)
    print(f'#{tc} {result}')

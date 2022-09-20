def permutation(n, m , arr):
    global stack
    stack.append(n)
    arr.remove(n)
    arr_c = arr[:]
    if len(stack) == m:
        print(*stack)
        stack.pop()
        arr.append(n)
        arr.sort()
        return
    for num in arr_c:
        permutation(num, m, arr)
    stack.pop()
    arr.append(n)
    arr.sort()
    return

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
stack = []

for i in range(1, N + 1):
    permutation(i, M, arr)

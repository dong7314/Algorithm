def checking(n):
    for i in range(n + 1):
        num = i ** 3
        if num == n:
            return i
        if num > n:
            return -1
    return -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc} {checking(N)}')

# import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    result = 'Possible'
    bread = 0
    i = 0
    for s in range(0, arr[-1] + 1):
        if s % M == 0 and s != 0:
            bread += K
        while i < N and s == arr[i]:
            if bread > 0:
                bread -= 1
                i += 1
            else:
                result = 'Impossible'
                break

    print(f'#{tc} {result}')


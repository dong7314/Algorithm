T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o' and j + 4 < N and i + 4 < N:
                if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4]:
                    flag = 'YES'
            if arr[i][j] == 'o' and j - 4 < N and i + 4 < N:
                if arr[i][j] == arr[i+1][j-1] == arr[i+2][j-2] == arr[i+3][j-3] == arr[i+4][j-4]:
                    flag = 'YES'
            if arr[i][j] == 'o' and j + 4 < N:
                if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4]:
                    flag = 'YES'
            if arr[i][j] == 'o' and i + 4 < N:
                if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j]:
                    flag = 'YES'

    print(f'#{tc} {flag}')

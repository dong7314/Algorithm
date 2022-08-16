def gugudan(A, B):
    if A >= 10 or B >= 10:
        return -1
    return A * B

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'#{tc} {gugudan(A, B)}')




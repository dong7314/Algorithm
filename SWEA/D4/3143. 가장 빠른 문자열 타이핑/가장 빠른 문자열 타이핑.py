T = int(input())
for tc in range(1, T + 1):
    A, B = map(str, input().split())

    cnt = 0
    skip = -1
    for i in range(len(A)):
        if i <= skip:
            continue
        if A[i:i + len(B)] == B:
            skip = i + len(B) - 1
        cnt += 1

    print(f'#{tc} {cnt}')

def card(kind, num):
    if kind == 'S':
        S[num] += 1
    elif kind == 'D':
        D[num] += 1
    elif kind == 'H':
        H[num] += 1
    elif kind =='C':
        C[num] += 1

def checking():
    for n in S:
        if n > 1:
            return 'ERROR'
    for n in D:
        if n > 1:
            return 'ERROR'
    for n in H:
        if n > 1:
            return 'ERROR'
    for n in C:
        if n > 1:
            return 'ERROR'

    return [13 - sum(S), 13 - sum(D), 13 - sum(H), 13 - sum(C)]

T = int(input())
for tc in range(1, T + 1):
    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14
    temp = input()
    for i in range(0, len(temp), 3):
        kind = temp[i]
        num = int(temp[i + 1:i + 3])
        card(kind, num)

    check = checking()
    print(f'#{tc}', end=' ')
    if checking() != 'ERROR':
        print(*check)
    else:
        print(check)

for _ in range(10):
    Number = int(input())
    pattern = input()
    text = input()

    N = len(text)
    M = len(pattern)
    i = 0
    j = 0
    cnt = 0
    while i < N:
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == M:
            j = 0
            cnt += 1

    print(f'#{Number} {cnt}')

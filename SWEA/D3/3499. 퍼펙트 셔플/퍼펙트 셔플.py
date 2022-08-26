T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    half = N // 2
    if N % 2 == 0:
        deck1 = arr[0:half]
        deck2 = arr[half:N]
    else:
        deck1 = arr[0:half + 1]
        deck2 = arr[half + 1:N]

    shuffle = []
    for i in range(half):
        shuffle.append(deck1[i])
        shuffle.append(deck2[i])
        if i == half - 1 and N % 2 == 1:
            shuffle.append(deck1[i + 1])

    print(f'#{tc}', end=' ')
    print(*shuffle)

T = int(input())
for tc in range(1, T + 1):
    N, R = input().split()
    R = int(R)

    arr_set = {tuple(N)}
    for _ in range(R):
        for a in list(arr_set):
            arr_set.remove(a)
            a = list(a)
            for i in range(len(a) - 1):
                for j in range(i + 1, len(a)):
                    a[i], a[j] = a[j], a[i]
                    arr_set.add(tuple(a))
                    a[i], a[j] = a[j], a[i]

    arr_list = []
    for a in list(arr_set):
        arr_list.append(int(''.join(a)))
    print(f'#{tc} {max(arr_list)}')

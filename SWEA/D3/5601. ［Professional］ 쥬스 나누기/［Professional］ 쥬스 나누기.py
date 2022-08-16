T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = []

    # 사람 수 만큼 반복시켜 나눈 음료수를 arr 배열에 담는다.
    for _ in range(N):
        arr.append(f'1/{N}')

    print(f'#{tc}', end=' ')
    # 사람 수대로 arr에서 음료수를 선택해 뽑아낸 값을 출력한다.
    for _ in range(N):
        amount = arr.pop()
        print(amount, end=' ')
    print()



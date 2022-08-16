T = int(input())
for tc in range(1, T + 1):
    arr = list(input())

    # a, b를 1로 초기화
    a = b = 1
    # 배열로 받은 문자열들을 하나씩 꺼낸다
    for word in arr:
        # 만약 L이라면 b를 변경
        if word == 'L':
            b = a + b
        # 만약 R이라면 a를 변경
        else:
            a = a + b

    print(f'#{tc} {a} {b}')



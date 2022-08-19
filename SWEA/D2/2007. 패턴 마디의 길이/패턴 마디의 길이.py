T = int(input())
for tc in range(1, T + 1):
    text = list(input())

    pattern = []        # pattern 리스트
    k = 0               # text에서 뽑아낼 인덱스 값
    while True:
        cnt = 0         # 반복이 되는 횟수
        # pattern 리스트에 while이 반복되면서 text의 글자를 한자씩 넣는다
        pattern.append(text[k])
        # pattern의 수만큼 index를 증가시키면서 text를 for문으로 돌린다.
        for i in range(0, len(text), len(pattern)):
            # pattern의 길이만큼 text의 값과 비교해서 다르다면
            # k를 1증가시키고 for문을 정지시킨다.
            if text[i:i + len(pattern)] != pattern:
                k += 1
                break
            # 같다면 cnt값을 1 증가
            else:
                cnt += 1
        # 반복 횟수가 2이상이라면 while문을 정지시킨다.
        if cnt > 1:
            break

    print(f'#{tc} {len(pattern)}')
T = 10
SIZE = 100
for tc in range(1, T + 1):
    number = input()
    arr = [list(input()) for _ in range(SIZE)]
    arr_c = list(zip(*arr))

    max_len = 0
    for i in range(SIZE): # row
        for j in range(SIZE): # column
            # j를 기준으로 마지막 인덱스까지 단어를 뽑아내 회문 검사를 실시하는 for문
            for k in range(j + 1, SIZE + 1):
                word_row = arr[i][j:k]
                word_column = arr_c[i][j:k]
                if word_row == word_row[::-1]:
                    if len(word_row) > max_len:
                        max_len = len(word_row)
                if word_column == word_column[::-1]:
                    if len(word_column) > max_len:
                        max_len = len(word_column)

    print(f'#{tc} {max_len}')
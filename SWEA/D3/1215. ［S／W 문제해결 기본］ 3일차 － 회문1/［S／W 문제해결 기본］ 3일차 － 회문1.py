# 길이에 따른 회문 판단 함수
# return은 회문의 개수
def palindrome(list, length):
    count = 0
    for word in list:
        for i in range(len(word) - length + 1):
            cutting_word = word[i:i+length]
            if cutting_word == cutting_word[::-1]:
                count += 1
    return count

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    # 가로줄 리스트 생성
    row_words_list = []
    for _ in range(8):
        row = input()
        row_words_list.append(row)

    # 세로줄을 담는 리스트 생성
    column_words_list = []
    for i in range(8):
        column_words = ''
        for j in range(8):
            # column_words에 한 자씩 담는다
            column_words += row_words_list[j][i]
        # column list에 각각 완성된 한 줄을 담는다.
        column_words_list.append(column_words)
    
    print(f'#{test_case} {palindrome(row_words_list, length) + palindrome(column_words_list, length)}')
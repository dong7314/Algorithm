def code_find(code):
    idx = code.rfind('1')
    if idx == -1:
        return []
    code = code[idx - 55:idx + 1]
    changing_num = []
    for i in range(8):
        arr = []
        code_number = code[i * 7:(i + 1) * 7]
        count = 1
        for j in range(7):
            if j == 6:
                arr.append(count)
            elif code_number[j] == code_number[j + 1]:
                count += 1
            else:
                arr.append(count)
                count = 1
        for key, value in pw_dict.items():
            if value == arr:
                changing_num.append(key)
    
    return changing_num

def checking_code(arr):
    odd_sum = 0
    even_sum = 0
    for i in range(7):
        if i % 2:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]
    if ((odd_sum * 3) + even_sum + arr[7]) % 10 == 0:
        return True
    else:
        return False

pw_dict = {
        0:[3, 2, 1, 1], 
        1:[2, 2, 2, 1], 
        2:[2, 1, 2, 2],
        3:[1, 4, 1, 1],
        4:[1, 1, 3, 2],
        5:[1, 2, 3, 1],
        6:[1, 1, 1, 4],
        7:[1, 3, 1, 2],
        8:[1, 2, 1, 3],
        9:[3, 1, 1, 2]    
}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = list(map(int, input().split()))
    result = 0
    while n > 0:
        n -= 1
        code = input()
        alter_code = code_find(code)
        if not alter_code:
            continue
        confirm = checking_code(alter_code)
        if confirm == True:
            result = sum(alter_code)
        else:
            result = 0	

    print(f'#{test_case} {result}')
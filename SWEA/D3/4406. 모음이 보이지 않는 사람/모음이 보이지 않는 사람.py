T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = input()
    vowels = 'aeiou'
    transform = ''
    
    for word in words:
        if word in vowels:
            continue
        transform += word
        
    print(f'#{test_case} {transform}')
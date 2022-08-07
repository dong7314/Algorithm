T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    height = list(map(int, input().split()))

    for _ in range(n):
        max_height = max(height)
        min_height = min(height)
        height[height.index(max_height)] = max_height - 1
        height[height.index(min_height)] = min_height + 1
    print(f'#{test_case} {max(height) - min(height)}')
    # ///////////////////////////////////////////////////////////////////////////////////

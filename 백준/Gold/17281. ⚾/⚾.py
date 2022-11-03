def perm(n, k):
    if n == k:
        order_p = p[:3] + [1] + p[3:]
        order_list.append(order_p)
    else:
        for i in range(8):
            if p[n] == 0 and visited[i] == 0:
                visited[i] = 1
                p[n] = baseball_number[i]
                perm(n + 1, k)
                visited[i] = 0
                p[n] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0     # 정답

# 배열 순서를 정할 때 필요한 목록들
baseball_number = [2, 3, 4, 5, 6, 7, 8, 9]
visited = [0] * 8
p = [0] * 8
order_list = []

# 배열의 순서들을 order_list에 담는 함수
perm(0, 8)

# 게임 실행
for i in range(len(order_list)):    # i는 타자 순서 전체를 담은 order_list의 인덱스 번호
    order = order_list[i]           # 타자 순서를 담은 리스트
    last_hitter = 0                 # 마지막으로 멈춘 타자를 적는다.
    total_score = 0
    for j in range(N):  # j는 이닝 번호
        score = arr[j]  # score는 이닝 때 타자들이 칠 수 있는 안타
        k = last_hitter # 타순
        out_count = 0   # out 카운트 3이 되면 정지 되도록 실행
        base1 = base2 = base3 = base4 = 0
        while out_count != 3:   # out_count가 3이 되면 정지
            result = score[order[k] - 1]    # 안타의 결과
            if result == 0:             # 안타 결과가 0이라면 out 처리를 한다.
                out_count += 1
            else:
                # 주루가 없는 곳에 안타를 친 타수를 넣는 과정
                base_in = 0
                if base1 == 0:
                    base1 = result
                    base_in = 1
                elif base2 == 0:
                    base2 = result
                    base_in = 2
                elif base3 == 0:
                    base3 = result
                    base_in = 3
                elif base4 == 0:
                    base4 = result
                    base_in = 4

                # 타수를 넣었다면 이미 타수가 나가 있는 주루에 안타를 넣어준다.
                if base1:
                    if base_in != 1:
                        base1 += result
                    if base1 > 3:
                        total_score += 1
                        base1 = 0
                if base2:
                    if base_in != 2:
                        base2 += result
                    if base2 > 3:
                        total_score += 1
                        base2 = 0
                if base3:
                    if base_in != 3:
                        base3 += result
                    if base3 > 3:
                        total_score += 1
                        base3 = 0
                if base4:
                    if base_in != 4:
                        base4 += result
                    if base4 > 3:
                        total_score += 1
                        base4 = 0
            k += 1
            if k > 8: k = 0
            last_hitter = k

    if total_score > ans:
        ans = total_score

print(ans)

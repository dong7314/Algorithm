def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def kruskal():
    cnt = 0  # 간선갯수
    total = 0  # 가중치의 합

    for i in range(len(arr)):  # MST 구성을 위해 V의 간선 선택
        p1 = find_set(arr[i][0])  # 두 정점의 대표원소 알아내기
        p2 = find_set(arr[i][1])
        if p1 != p2:  # 싸이클이 생기지 않는다.
            total += arr[i][2]  # MST에 포함된 간선의 가중치 추가
            cnt += 1  # 간선의 개수 증가
            p[p2] = p1  # union
        if cnt == N: break  # 0 ~ V까지 정점을 가짐(정점-1)
    return total

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))     # X 좌표 리스트
    Y = list(map(int, input().split()))     # Y 좌표 리스트
    E = float(input())                      # 세율
    arr = []

    for i in range(N - 1):
        first_x = X[i]
        first_y = Y[i]
        for j in range(i + 1, N):
            second_x = X[j]
            second_y = Y[j]
            value = ((first_x - second_x) ** 2 + (first_y - second_y) ** 2) * E
            arr.append([i, j, value])

    arr.sort(key=lambda x: x[2])  # 간선의 가중치로 정렬
    p = [i for i in range(N + 1)]  # make-set
    print(f'#{tc} {round(kruskal())}')


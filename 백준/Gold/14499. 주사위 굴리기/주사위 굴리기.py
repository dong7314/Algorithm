N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
k_arr = list(map(int, input().split()))
dice = [1, 3, 4, 2, 5, 6]
dice_value = [0] * 7

# 동, 서, 북, 남, 최상단 순으로 배열 생성
dice_dict = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


dice_face = 1
# 1, 2, 3, 4 순으로 동 서 북 남이다.
for i in range(K):
    move_dice = [0] * 6
    way = k_arr[i]
    if 0 <= x + dx[way] < N and 0 <= y + dy[way] < M:
        x = x + dx[way]
        y = y + dy[way]
        dice_face = dice[way]
        if way == 1:
            move_dice[0] = dice_face
            move_dice[1] = dice_dict[dice[0]]
            move_dice[2] = dice[0]
            move_dice[3] = dice[3]
            move_dice[4] = dice[4]
            move_dice[5] = dice_dict[dice_face]
        elif way == 2:
            move_dice[0] = dice_face
            move_dice[1] = dice[0]
            move_dice[2] = dice_dict[dice[0]]
            move_dice[3] = dice[3]
            move_dice[4] = dice[4]
            move_dice[5] = dice_dict[dice_face]
        elif way == 3:
            move_dice[0] = dice_face
            move_dice[1] = dice[1]
            move_dice[2] = dice[2]
            move_dice[3] = dice_dict[dice[0]]
            move_dice[4] = dice[0]
            move_dice[5] = dice_dict[dice_face]
        elif way == 4:
            move_dice[0] = dice_face
            move_dice[1] = dice[1]
            move_dice[2] = dice[2]
            move_dice[3] = dice[0]
            move_dice[4] = dice_dict[dice[0]]
            move_dice[5] = dice_dict[dice_face]
        dice = move_dice

        print(dice_value[dice_dict[dice_face]])
        if arr[x][y] == 0:
            arr[x][y] = dice_value[dice_face]
        else:
            dice_value[dice_face] = arr[x][y]
            arr[x][y] = 0
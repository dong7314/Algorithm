T = int(input())
for tc in range(1, T + 1):
    order, num = input().split()
    arr = input().split()

    count_list = [0] * 10
    GNS_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    GNS_reverse_dict = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}

    for words in arr:
        count_list[GNS_dict[words]] += 1

    print(order)
    for i in range(10):
        for j in range(count_list[i]):
            print(GNS_reverse_dict[i], end=' ')
    print()


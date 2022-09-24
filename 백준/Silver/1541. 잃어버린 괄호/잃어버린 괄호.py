cal = input()

num = ''
num_list = []
cal_list = []
for i in range(len(cal)):
    if i == len(cal) - 1:
        num += cal[i]
        num_list.append(int(num))
    if cal[i].isdigit():
        num += cal[i]
    else:
        num_list.append(int(num))
        cal_list.append(cal[i])
        num = ''

while len(cal_list):
    idx = -1
    for i in range(len(cal_list)):
        if cal_list[i] == '+':
            idx = i

    if idx != -1:
        while idx < len(cal_list):
            if cal_list[idx] == '+':
                num_list[idx] = num_list[idx] + num_list[idx + 1]
                num_list.pop(idx + 1)
                cal_list.pop(idx)
                idx += 1
            else:
                break
    else:
        n = 0
        for _ in range(len(cal_list)):
            num_list[n] = num_list[n] - num_list[n + 1]
            num_list.pop(n + 1)
            cal_list.pop(n)

print(num_list[0])
'''
5
0 1 1 3 2
둘째줄은 뽑은 번호
'''
N = int(input())
arr = list(map(int, input().split()))
student = []


for i in range(N):
    student.insert(i - arr[i], i + 1)
print(*student)

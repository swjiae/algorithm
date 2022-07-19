T = int(input())
print(f'#{T}')
for i in range(int(input())):
    a = list(input().split())
    n = 1
    while n <= int(a[1]):
        print(a[0], end = '')
        n = n + 1
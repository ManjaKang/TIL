T = int(input())
for _ in range(T):
    arr = input().split()
    for ch in arr[1]:
        print(ch * int(arr[0]), end='')
    print()
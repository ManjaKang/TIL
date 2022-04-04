N = int(input())
nums_n = list(map(int, input().split()))
M = int(input())
nums_m = list(map(int, input().split()))

for m in nums_m:
    if m in nums_n:
        print(1)
    else:
        print(0)
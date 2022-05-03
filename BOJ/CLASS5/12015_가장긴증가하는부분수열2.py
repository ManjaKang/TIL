import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
memo = [0]

for a in arr:
    if a > memo[-1]:
        memo.append(a)
    else:
        left = 0
        right = len(memo)
        while left < right:
            mid = (right + left) // 2
            if memo[mid] < a:
                left = mid + 1
            else:
                right = mid
        memo[right] = a

print(len(memo)-1)
# PyPy 436 ms
from collections import defaultdict
N = int(input())
A, B = map(int, input().split())
arr_a = [int(input()) for _ in range(A)]
arr_b = [int(input()) for _ in range(B)]
arr_a = [0] + arr_a + arr_a[:-2]        # 회전을 고려하기 위한 작업
arr_b = [0] + arr_b + arr_b[:-2]
case_dict_a = defaultdict(int)
case_dict_b = defaultdict(int)
ans = 0

# 누적합
for i in range(1, len(arr_a)):
    arr_a[i] += arr_a[i-1]
for i in range(1, len(arr_b)):
    arr_b[i] += arr_b[i-1]

# 누적합에서 각 피자에서 나올 수 있는 모든 경우의 수 구하기
for i in range(1, A):
    for j in range(A):
        temp = arr_a[i+j] - arr_a[j]
        case_dict_a[temp] += 1
case_dict_a[arr_a[A]] += 1              # 피자 전체를 선택한 경우 추가

for i in range(1, B):
    for j in range(B):
        temp = arr_b[i+j] - arr_b[j]
        case_dict_b[temp] += 1
case_dict_b[arr_b[B]] += 1

for size, num_case in case_dict_a.items():
    if size > N:
        continue
    elif size == N:
        ans += num_case
    else:
        ans += case_dict_b[N-size] * num_case

ans += case_dict_b[N]       # B 피자 전체를 선택하는 경우 추가
print(ans)
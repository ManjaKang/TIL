N = int(input())
for _ in range(N):
    ox = input()
    ans = 0
    idx = 0
    for ch in ox:
        if ch == 'O':
            idx += 1
        else:
            idx = 0
        ans += idx
    print(ans)
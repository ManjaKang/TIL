N, M = map(int, input().split())
didnt_hear = set()
didnt_see = set()
for _ in range(N):
    didnt_hear.add(input())
for _ in range(M):
    didnt_see.add(input())

didnt_hear_see = didnt_hear.intersection(didnt_see)
print(len(didnt_hear_see))
didnt_hear_see = list(didnt_hear_see)
didnt_hear_see.sort()
print(*didnt_hear_see, sep='\n')
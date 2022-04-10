N, M = map(int, input().split())

pokemon = {}
for i in range(1, N+1):
    name = input()
    pokemon[name] = i
    pokemon[str(i)] = name

for _ in range(M):
    ask = input()
    print(pokemon.get(ask))
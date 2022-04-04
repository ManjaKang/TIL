N = int(input())
movie_list = ['666']
for i in range(1, N):
    temp = movie_list[i-1]
    temp = str(int(temp) + 1)
    while '666' not in temp:
        temp = str(int(temp) + 1)
    movie_list.append(temp)
print(movie_list[N-1])
N = int(input())
for _ in range(N):
    word = input()
    left = 0
    right = len(word) - 1
    flag = False
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        elif word[left] == word[right-1] and not flag:
            right -= 1
            flag = True
        elif word[left+1] == word[right] and not flag:
            left += 1
            flag = True
        else:
            print(2)
            break
    else:
        if flag:
            print(1)
        else:
            print(0)
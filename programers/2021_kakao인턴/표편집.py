def move(arr, k, i, direct):
    idx = 0
    while idx != i:
        k += direct
        if arr[k] == 'O':
            idx += 1
    return k


def solution(n, k, cmd):
    arr = ['O'] * n
    prev = 0
    stack = []
    for c in cmd:
        if c[0] == 'C':
            arr[k] = 'X'
            stack.append(k)
            if k == n - 1:
                k = move(arr, k, 1, -1)
            else:
                k = move(arr, k, 1, 1)
        elif c[0] == 'Z':
            arr[stack.pop()] = 'O'
        else:
            d, i = c.split()
            i = int(i)
            if c[0] == 'D':
                k = move(arr, k, i, 1)
            else:
                k = move(arr, k, i, -1)
    return ''.join(arr)


cmd = 	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8, 2, cmd))
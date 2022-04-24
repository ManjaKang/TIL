from pprint import pprint


def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
M = len(key)
N = len(lock)
ans_key = ''
for i in range(N):
    for j in range(N):
        if lock[i][j]:
            ans_key += '0'
        else:
            ans_key += '1'
key_arr1 = [[0]*(M+2*N-2) for _ in range((M+2*N-2))]
for i in range(M):
    for j in range(M):
        key_arr1[i+N-1][j+N-1] = key[i][j]

key_arr2 = rotate(key_arr1)
key_arr3 = rotate(key_arr2)
key_arr4 = rotate(key_arr3)
bin_list = []
for i in range(N+M-1):
    for j in range(N+M-1):
        temp_str1 = ''
        temp_str2 = ''
        temp_str3 = ''
        temp_str4 = ''
        for a in range(N):
            for b in range(N):
                temp_str1 += str(key_arr1[i+a][j+b])
                temp_str2 += str(key_arr2[i+a][j+b])
                temp_str3 += str(key_arr3[i+a][j+b])
                temp_str4 += str(key_arr4[i+a][j+b])
        bin_list.extend([temp_str1, temp_str2, temp_str3, temp_str4])

import sys
from pprint import pprint
sys.stdin = open('sampleinput.txt', 'r')


def
T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    a_dict = dict()
    si = 0
    sj = 0
    idx = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '_' and arr[i][j] != '#':
                a_dict[(i, j)] = idx
                idx += 1
                if arr[i][j] == 'S':
                    si = i
                    sj = j


    pprint(a_dict)
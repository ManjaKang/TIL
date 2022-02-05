import copy

def serch(map_list, y, x):
    force = map_list[y][x]
    map_list[y][x] = 0
    for a in range(1,force):
        if x-a >= 0:
            if map_list[y][x-a] > 1:
                serch(map_list, y, x-a)
            else:
                map_list[y][x-a] = 0
        if y-a >= 0:
            if map_list[y-a][x] > 1:
                serch(map_list, y-a, x)
            else:
                map_list[y-a][x] = 0
        if x+a < W:
            if map_list[y][x+a] > 1:
                serch(map_list, y, x+a)
            else:
                map_list[y][x+a] = 0
        if y+a < H:
            if map_list[y+a][x] > 1:
                serch(map_list, y+a, x)
            else:
                map_list[y+a][x] = 0
    return map_list

def drop_marble(map_list, x):
    for y in range(len(map_list)):
        if map_list[y][x] == 0:
            continue
        if map_list[y][x] == 1:
            map_list[y][x] = 0
            break
        if map_list[y][x] > 1:
            serch(map_list, y, x)
            break
    return map_list

def make_case(w, x, n):
    result_list = [i//(w**(x-1)) for i in range(w**x)] * w**(n - x)
    return result_list

def make_permutation(w, n):
    case_list = []
    for i in range(1, n+1):
        case_list.append(make_case(w,i,n))
    return tuple(zip(*case_list))
                
def clean_map(map_list,h):
    new_list = list(map(list, zip(*map_list)))
    for line in new_list:
        while 0 in line:
	        line.remove(0)
        while len(line) < h:
            line.insert(0,0)
    result_list = list(map(list, zip(*new_list)))
    return result_list
            
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().rstrip().split(' '))
    li_list = []
    for i in range(H):
        li_list.append(list(map(int, input().rstrip().split(' '))))
    #입력 완료
    case_list = list(make_permutation(W,N))
    cnt_list = []
    for case in case_list:
        temp_map = copy.deepcopy(li_list)
        cnt = 0
        for i in case:
            temp_map = drop_marble(temp_map, i)
            temp_map = clean_map(temp_map, H)
        for y in temp_map:
            for x in y:
                if x != 0:
                    cnt += 1
        cnt_list.append(cnt)
    min_cnt = min(cnt_list)
    print('#{} {}'.format(test_case, min_cnt))


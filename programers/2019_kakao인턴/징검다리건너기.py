def check(stones, k, n):
    stones = stones[:]
    cnt = 0
    for stone in stones:
        if stone - n < 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True


def solution(stones, k):
    left = 0
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        if check(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

'''
Test 1 〉	통과 (287.01ms, 19MB)
Test 2 〉	통과 (350.93ms, 19MB)
Test 3 〉	통과 (320.17ms, 19MB)
Test 4 〉	통과 (179.24ms, 18.8MB)
Test 5 〉	통과 (227.57ms, 19MB)
Test 6 〉	통과 (230.65ms, 19MB)
Test 7 〉	통과 (404.28ms, 18.7MB)
Test 8 〉	통과 (445.53ms, 19.1MB)
Test 9 〉	통과 (423.09ms, 19.1MB)
Test 10 〉	통과 (407.16ms, 18.9MB)
Test 11 〉	통과 (370.69ms, 18.9MB)
Test 12 〉	통과 (407.45ms, 19MB)
Test 13 〉	통과 (266.96ms, 19.1MB)
Test 14 〉	통과 (217.10ms, 19MB)
'''
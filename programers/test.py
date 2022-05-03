from collections import deque

arr = [1, 4, 5, 10, 11]
arr = deque(arr)
arr.rotate(5-1-1)
print(arr)
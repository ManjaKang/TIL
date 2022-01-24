i = int(input())
cnt = 0
for a in range(1,i+1):
    if i % a == 0:
        print("%d(은)는 %d의 약수입니다."%(a,i))
        cnt += 1
if cnt == 2:
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." %(i,i))

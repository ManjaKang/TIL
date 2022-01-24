score = [88,30,61,55,95]
for idx, val in enumerate(score):
    if val >= 60:
        print("%d번 학생은 %d점으로 합격입니다."%(idx+1,val))
    else:
        print("%d번 학생은 %d점으로 불합격입니다."%(idx+1,val))

def solution(files):
    sorted_files = []
    answer = []
    for idx, file in enumerate(files):
        sorted_files.append((sep(file, idx)))
    sorted_files.sort()
    for file in sorted_files:
        answer.append(files[file[-1]])      # file[-1]에는 파일들의 인덱스가 저장되 었음
    return answer


# 파일명을 헤드, 넘버, 파일명인덱스로 변환하는 함수
def sep(file: str, i):
    number_start = 100000
    tail_start = 100000
    for idx in range(len(file)):
        if file[idx].isdigit():
            number_start = idx
            break
    for idx in range(number_start, len(file)):
        if not file[idx].isdigit():
            tail_start = idx
            break
    return file[:number_start].upper(), int(file[number_start:tail_start]), i


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

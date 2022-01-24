class Student:
    def __init__(self, kor, mat, eng):
        self.__kor = kor
        self.__mat = mat
        self.__eng = eng
 
    @property
    def kor(self):
        return self.__kor
 
    @property
    def mat(self):
        return self.__mat
 
    @property
    def eng(self):
        return self.__eng
 
    def get_total(self):
        return self.__kor + self.__mat + self.__eng
 
 
t_str = input()
t_str = t_str.split(", ")
t_str = list(map(int, t_str))
student = Student(t_str[0], t_str[1], t_str[2])
print("국어, 영어, 수학의 총점: {0}".format(student.get_total()))

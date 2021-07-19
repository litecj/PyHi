'''
국어 kor, 영어 eng, 수학 math를 입력받아서 평균점수를 통해 A-F
학생이름, 총점, 평균 점수, 학점(A-F)
'''




class Grade(object):
    def __init__(self,kor,eng,math,average):
        self.kor = kor
        self.eng = eng
        self.math = math
        #self.average = self.kor+self.eng+self.math/3

    #def average(self):
     #   return self.kor+self.eng+self.math/3

    @staticmethod
    def main():
        kor = int(input('국어점수 :'))
        eng = int(input('영어점수 :'))
        math = int(input('수학점수 :'))
        average = (kor + eng + math)/3
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        elif average >= 50:
            grade = 'E'
        else:
            grade = 'F'
        print(grade)

Grade.main()
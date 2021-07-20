'''
국어 kor, 영어 eng, 수학 math를 입력받아서 평균점수를 통해 A-F
학생이름, 평균 점수, 학점(A-F)
'''
class Grade(object):
    def __init__(self,name):
        self.name = name
        self.scores = []

    def addScores(self,score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    @staticmethod
    def main():
        grades = Grade(input('name:'))
        for i in ['kor', 'eng', 'math']:
            grades.addScores(int(input(f'{i}:')))
        average = grades.avg()
        if average >= 90:
            AF = 'A'
        elif average >= 80:
            AF = 'B'
        elif average >= 70:
            AF = 'C'
        elif average >= 60:
            AF = 'D'
        elif average >= 50:
            AF = 'E'
        else:
            AF = 'F'
        print(f'이름 :{grades.name} 평균 : {average} \n학점 : {AF}\n')

Grade.main()
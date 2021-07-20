'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
출력은 "안녕하세요, 제 이름은 TOM이고, 나이는 28세이고, 서울에 거주합니다."로 됩니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''

'''
class Person (object):
    def __init__(self):
        self.persons = []

    def pr(self):
        return print(f'안녕하세요. 제 이름은 {persons[0]}이고, 나이는{persons[1]}세이고,{persons[2]}에서 거주합니다.\n')


    @staticmethod
    def main():
        persons = Person(input('name : '))
        for i in ['이름', '나이', '사는 곳']:
            persons.pr(int(input(f'{i}')))

Person.main()
'''

class Person(object):
    def __init__(self, name, age, live):
        self.name = name
        self.age = age
        self.live = live

    def pr(self):
        return print(f'\n안녕하세요. 제 이름은 {self.name}이고, 나이는{self.age}세이고,{self.live}에서 거주합니다.\n')

    @staticmethod
    def main():
        persons = []
        while 1:
            menu = input('0.종료  1.등록  2.목룍')
            if menu == '0':
                return
            elif menu == '1':
                persons.append(Person(input('name'),input('age'),input('live')))
            elif menu == '2':
                for i in persons:
                    i.pr()

Person.main()
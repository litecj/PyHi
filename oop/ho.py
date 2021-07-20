class Person1 (object):
    def __init__(self, name, age, live):
        self.name = name
        self.age = age
        self.live = live

    def pr(self):
        return print(f'안녕하세요. 제 이름은 {self.name}입니다. 저는 {self.age}살이고, {self.live}에 살고 있습니다.')


def main():
    persons = []
    while 1:
        menu = input('0.종료  1.등록  2.목록')
        if menu == '0':
            return
        elif menu == '1':
            persons.append(Person1(input('name'),input('age'),input('live')))
        elif menu == '2':
            for i in persons:
                i.pr()

if __name__ =='__main__':
    main()
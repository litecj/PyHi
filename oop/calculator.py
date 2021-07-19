class Calculator(object):
    # num1, num2 : 인스턴스 변수 생략 (굳이 사용 되지 않는 것 같아 없애자!!)

    def __init__(self, num1, num2):
        self.num1 = num1  # this  → self (java꺼 쓰기 싫어 ㅋ)
        self.num2 = num2

    """ Calculator():
        pass """

    def add(self):
        return self.num1+self.num2

    def subtract(self):
        return self.num1-self.num2

    def multiple(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2

    def remain(self):
        return self.num1%self.num2

    @staticmethod
    def main():
        while 1:
            menu = input('0-exit  1-Calculate\n')
            if menu =='0':
                return
            elif menu == '1':
                    num1 = int(input('first number:'))
                    opcode = input('+-*/% :')
                    num2 = int(input('second nubmer:'))
                    result = 0
                    calc = Calculator(num1, num2)
                    if opcode == '+':
                        result = calc.add()
                    elif opcode == '-':
                        result = calc.subtract()
                    elif opcode == '*':
                        result = calc.multiple()
                    elif opcode == '/':
                        result = calc.divide()
                    elif opcode == '%':
                        result = calc.remain()
                    print(f'{calc.num1}{opcode}{calc.num2} = {result}')
            else:
                print('Wrong Selected Number')
                break


Calculator.main()
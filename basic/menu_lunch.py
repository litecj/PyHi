import random


def menu_lunch ():
    menu = ["김치찌개", "샐러드", "쉐이크", "불백", "삼계탕", "도시락",
            "김밥", "국밥", "아사이볼", "본죽", "비빔밥", "수제비"]
    print(random.choice(menu))


if __name__ == '__main__':
    menu_lunch()
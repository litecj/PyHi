from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

'''
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
① like  -  "lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다. - coin, 주식
'''
class Melon (object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers ={'User-Agent':'Mozilla/5.0'})), 'lxml')
        n_rank = 0
        ls = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        ls2 = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        print(f'List size is {len(ls)}')
        for i, j in enumerate(ls):
            n_rank += 1
            print(str(n_rank) + "Rank", j.find('a').text,':',ls2[i].find('a').text)

def main():
    Melon(f'https://www.melon.com/chart/index.htm?dayTime={input("Input Date")}{input("Input Hour")}').scrap()


if __name__ == '__main__':
    main()


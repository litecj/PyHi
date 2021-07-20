from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
① like  -  "lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다. - coin, 주식
'''
class BugsMucis (object):

    def __init__(self, url):
        self.url = url


    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artists = 0
        n_title = 0
        ls = soup.find_all(name='p', attrs={'class': 'artist','class':'title'})
        #ls2 = soup.find_all(name='p', attrs={'class':'artist'})
        #ls3 = ls + ls2
        print(f'List size is {len(ls)}')
        for i in ls:
            n_title += 1
            n_artists += 1
            print(str(n_title)+":")
            #print(str(n_artists)+"Rank",i.find('a').text,i.find('a').text)
            print(i.find('a').text)

def main():
    BugsMucis(f'https://music.bugs.co.kr/chart/track/realtime/total?chartdate={20210720}&charthour={16}').scrap()



if __name__ == '__main__':
    main()

    #input("Input Date")
    #input("Input Hour")
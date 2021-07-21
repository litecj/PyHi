from bs4 import BeautifulSoup
import requests
import pandas as pd
#from urllib.request import urlopen
#from urllib.request import Request


class mucisRanking (object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_url(self,detail):
        self.url = requests.get(f'{self.url}{detail}',headers=self.headers).text
        #mucisRanking=(f'https://www.melon.com/chart/index.htm?dayTime={input("Input Date")}{input("Input Hour")}')
    def get_raking(self):
        soup = BeautifulSoup(self.url,'lxml')
        n_rank = 0
        ls = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        ls2 = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        print(f'List size is {len(ls)}')
        for i, j in enumerate(ls):
            n_rank += 1
            print(str(n_rank) + "Rank", j.find('a').text, ':', ls2[i].find('a').text)
def main() :
    mr = mucisRanking()
    while 1:
        menu = input('0. exit, 1. input time, 2.output, 3.print dict, 4.dict to data to datafram, 5.df to csv\n')
        if menu == '0':
            return
        elif menu == '1':
            mr.set_url(f'https://www.melon.com/chart/index.htm?dayTime={input("Input Date")}{input("Input Hour")}')
        elif menu == '2':
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.get_raking()

        elif menu == '3':
            pass
        elif menu == '4':
            pass
        elif menu == '5':
            pass



if __name__ == '__main__':
    main()
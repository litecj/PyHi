from scraping.models.dataset import Dataset
from scraping.models.service import Service


class View (object):
    dataset = Dataset()
    service = Service()

    def modeling(self, melon, bugs):
        service = self.service
        this = self.preprocessing(melon, bugs)
        print(f'The Type of This is {type(this.melon)}')
        print(f'The head of melon is\n{this.melon.head(3)}')
        print(f'The head of bugs is\n{this.bugs.head(2)}')

    def preprocessing(self, melon, bugs) -> object:
        service = self.service
        this = self.dataset
        this.melon = service.model(melon)
        this.bugs = service.model(bugs)

        return this


if __name__ == '__main__':
    view = View()
    view.modeling('melon.csv', 'bugs.csv')
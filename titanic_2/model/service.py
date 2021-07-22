from titanic_2.model.dataset import Dataset
import pandas as pd


class Service (object):
    dataset = Dataset()

    def model(self, payload):
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
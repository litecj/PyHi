from titanic.model.dataset import Dataset
import pandas as pd

class Service (object) :

    dataset = Dataset()

    def new_model(self, payload: str) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

def create_train(this) -> {}:
    return this

def create_label(this) -> {}:
    return this

def drop_feature(this,*feature) ->(object):
    return this

def embarked_nominal(this)->(object):
    return this

def fare_oridnal(this)->(object):
    return this

def title_nominal(this)->(object):
    return this

def gender_nirminal(this)->(object):
    return this

def age_ordinal(this)->(object):
    return this

def create_k_fold(this) -> {}:
    return None

def accuracy_by_classfier(this) -> str:
    return ""
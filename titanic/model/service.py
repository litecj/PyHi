from titanic.model.dataset import Dataset
import pandas as pd

class Service (object) :

    dataset = Dataset()

    def new_model(self, payload: str) -> object:
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

def create_train(this:str) -> object:
    return this

def create_label(this:str) -> object:
    return this

def drop_feature(this,*feature):
    return this

def embarked_nominal(this):
    return this

def fare_oridnal(this):
    return this

def title_nominal(this):
    return this

def gender_nirminal(this):
    return this

def age_ordinal(this):
    return this

def create_k_fold(this:object) -> {}:
    return None

def accuracy_by_classfier(this):
    return ""
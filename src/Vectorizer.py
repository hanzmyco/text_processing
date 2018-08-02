from __future__ import print_function
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline
import config
import BaseModel


class CounterVector(BaseModel.BaseModel):
    def __init__(self,model):
        BaseModel.BaseMode.__init__(self,model)
        self.vectorizer = CountVectorizer()


class TfIdfVector(BaseModel.BaseModel):
    def __init__(self,model):
        BaseModel.BaseModel.__init__(self,model)
        if config.use_hashing:
            if config.use_idf:
                # Perform an IDF normalization on the output of HashingVectorizer
                hasher = HashingVectorizer(n_features=config.n_features,
                                           stop_words='english', alternate_sign=False,
                                           norm=None, binary=False)
                self.vectorizer = make_pipeline(hasher, TfidfTransformer())
            else:
                self.vectorizer = HashingVectorizer(n_features=config.n_features,
                                               # stop_words='english',
                                               alternate_sign=False, norm='l2',
                                               binary=False)
        else:
            self.vectorizer = TfidfVectorizer(max_df=0.5, max_features=config.n_features,
                                         min_df=1, stop_words='english',
                                         use_idf=True)




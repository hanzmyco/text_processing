from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
import config

class BaseModel(object):
    def __init__(self,model=None):
        self.model = model

    def feature_transform(self,data_in):
        self.feature = self.vectorizer.fit_transform(data_in)

        if config.n_components:
            svd = TruncatedSVD(config.n_components)
            normalizer = Normalizer(copy=False)
            lsa = make_pipeline(svd, normalizer)
            self.feature = lsa.fit_transform(self.feature)
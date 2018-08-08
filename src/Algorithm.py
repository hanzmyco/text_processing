from sklearn.externals import joblib
import config


class Base_Algorithm(object):
    def __init__(self,algo_name=None):
        self.algo_name = algo_name

    def fit(self, feature):
        self.algo.fit(feature)

    def serilize_model(self):
        file_name=config.model_file_name
        joblib.dump(self.algo,file_name)

    def de_serilize_model(self):
        self.algo = joblib.load(config.model_file_name)






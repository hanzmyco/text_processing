class Base_Algorithm(object):
    def __init__(self,algo_name):
        self.algo_name = algo_name

    def fit(self, feature):
        self.algo.fit(feature)




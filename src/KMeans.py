from sklearn.cluster import KMeans, MiniBatchKMeans
import Algorithm
import config

class KMeansClustering(Algorithm.Base_Algorithm):
    def __init__(self,algo_name):
        Algorithm.Base_Algorithm.__init__(self,algo_name)

        if config.minibatch:
            self.algo = MiniBatchKMeans(n_clusters=config.cluster_number, init='k-means++', n_init=1,
                         init_size=config.init_size, batch_size=config.batch_size, verbose=config.verbose)
        else:
            self.algo = KMeans(n_clusters=config.cluster_number, init='k-means++', max_iter=config.max_iter, n_init=1,
                               verbose=config.verbose)
        self.order_centroids = None

    def get_centroids(self,svd=None):
        if not config.use_hashing:
            print("Top terms per cluster:")
            if config.n_components:
                original_space_centroids = svd.inverse_transform(self.algo.cluster_centers_)
                self.order_centroids = original_space_centroids.argsort()[:, ::-1]
            else:
                self.order_centroids = self.algo.cluster_centers_.argsort()[:, ::-1]






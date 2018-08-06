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
            if config.n_components:
                original_space_centroids = svd.inverse_transform(self.algo.cluster_centers_)
                self.order_centroids = original_space_centroids.argsort()[:, ::-1]
            else:
                self.order_centroids = self.algo.cluster_centers_.argsort()[:, ::-1]


    def output_cluster_info(self,data_in,model,feed_id):
        index_dictionary = {}
        for index, label in enumerate(self.algo.labels_):
            if label not in index_dictionary:
                index_dictionary[label] = [index]
            else:
                index_dictionary[label].append(index)

        final_tuple = []
        terms = model.vectorizer.get_feature_names()
        with open(config.cluster_out_file, 'w', encoding='utf-8') as f:
            for label in range(0, config.cluster_number):
                f.write('cluster : ' + str(label) + '\n')
                for index in index_dictionary[label]:
                    f.write(data_in[index].strip(' ') + '\n')
                total_distance = sum(
                    [self.algo.score(model.feature[index]) for index in index_dictionary[label]])
                f.write('\n')

                targeted_feed_id = [feed_id[index] for index in index_dictionary[label]]
                term_list = set()
                for ind in self.order_centroids[label, :5]:
                    term_list.add(terms[ind])

                final_tuple.append([total_distance, label, targeted_feed_id, term_list])

            final_tuple.sort(reverse=True)

            '''
            check_list={}
            new_tuple=[]
            for index in range(0,len(final_tuple)):
                for index2 in range(0,final_tuple):
                    if index != index2 and index not in check_list :
                        total_diff=final_tuple[index][3]^final_tuple[index2][3]
                        if total_diff < config.diff_threshold:
                            new_tuple.append([ite[0]/2,ite[1].ite[2]+ite2[2],ite[3]])
            '''

            with open(config.top_terms_file, 'w', encoding='utf-8') as f:
                for index_tuples in final_tuple:
                    i = index_tuples[1]
                    f.write('Cluster' + str(i) + ':    ' + str(index_tuples[0]) + '    ')

                    f.write(str(index_tuples[3]) + ' ')
                    f.write('\n')
                    for feeds_id in index_tuples[2]:
                        f.write(feeds_id + '\n')
                    f.write('\n\n')










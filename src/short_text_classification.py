import config
import read_json
import Vectorizer
import KMeans
import BaseModel

def main():
    if config.model_name =='Counter':
        model = Vectorizer.CounterVector(config.model_name)
    elif config.model_name == 'TfIdf':
        model = Vectorizer.TfIdfVector(config.model_name)
        print('finish initilizing model')

    data_in=[]
    read_json.read_json(config.path_in,data_in,config.stop_word_path)
    model.feature_transform(data_in)

    if config.algo_name =='KMeans':
        algo_instance = KMeans.KMeansClustering(config.algo_name)
        algo_instance.fit(model.feature)

        terms=model.vectorizer.get_feature_names()
        algo_instance.get_centroids()

        with open(config.top_terms_file, 'w', encoding='utf-8') as f:
            for i in range(config.cluster_number):
                print("Cluster %d:" % i, end='')
                f.write('Cluster' + str(i) + ': ')
                # for ind in km.cluster_centers_[i,:5]:
                for ind in algo_instance.order_centroids[i, :5]:
                    print(' %s' % terms[ind], end='')
                    f.write(terms[ind] + ' ')
                f.write('\n')
                print()

        index_dictionary = {}
        for index, label in enumerate(algo_instance.algo.labels_):
            if label not in index_dictionary:
                index_dictionary[label] = [index]
            else:
                index_dictionary[label].append(index)

        print(index_dictionary)

        with open(config.cluster_out_file, 'w', encoding='utf-8') as f:
            for label in range(0, config.cluster_number):
                f.write('cluster : ' + str(label) + '\n')
                print('cluster ' + str(label) + ' : ')
                for index in index_dictionary[label]:
                    f.write(data_in[index].strip(' ') + '\n')
                    print(data_in[index].strip(' ') + '\n')
                print()
                f.write('\n')

if __name__ == '__main__':
    main()
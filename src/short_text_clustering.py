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
    feed_id=[]
    read_json.read_json(config.path_in,data_in,config.stop_word_path,feed_id,config.data_lines)
    model.feature_transform(data_in)

    if config.algo_name =='KMeans':
        algo_instance = KMeans.KMeansClustering(config.algo_name)
        algo_instance.fit(model.feature)

        terms=model.vectorizer.get_feature_names()
        algo_instance.get_centroids()

        index_dictionary = {}
        for index, label in enumerate(algo_instance.algo.labels_):
            if label not in index_dictionary:
                index_dictionary[label] = [index]
            else:
                index_dictionary[label].append(index)


        final_tuple=[]
        with open(config.cluster_out_file, 'w', encoding='utf-8') as f:
            for label in range(0, config.cluster_number):
                f.write('cluster : ' + str(label) + '\n')
                for index in index_dictionary[label]:
                    f.write(data_in[index].strip(' ') + '\n')
                total_distance=sum([algo_instance.algo.score(model.feature[index]) for index in index_dictionary[label]])
                f.write('\n')

                targeted_feed_id=[feed_id[index] for index in index_dictionary[label]]
                final_tuple.append([total_distance,label,targeted_feed_id])

            final_tuple.sort(reverse=True)

            with open(config.top_terms_file, 'w', encoding='utf-8') as f:
                for index_tuples in final_tuple:
                    i=index_tuples[1]
                    f.write('Cluster' + str(i) + ':    '+str(index_tuples[0])+'    ')
                    for ind in algo_instance.order_centroids[i, :5]:
                        f.write(terms[ind] + ' ')
                    f.write('\n')
                    for feeds_id in index_tuples[2]:
                        f.write(feeds_id+'\n')
                    f.write('\n\n')

if __name__ == '__main__':
    main()
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
    print('finish reading data')
    model.feature_transform(data_in)


    if config.algo_name =='KMeans':
        algo_instance = KMeans.KMeansClustering(config.algo_name)
        print('start training model')
        algo_instance.fit(model.feature)
        algo_instance.serilize_model()
        algo_instance.get_centroids()
        algo_instance.output_cluster_info(data_in,model,feed_id)




        '''
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
                term_list=set()
                for ind in algo_instance.order_centroids[label, :5]:
                    term_list.add(terms[ind])

                final_tuple.append([total_distance,label,targeted_feed_id,term_list])

            final_tuple.sort(reverse=True)
         '''

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

        '''
            with open(config.top_terms_file, 'w', encoding='utf-8') as f:
                for index_tuples in final_tuple:
                    i=index_tuples[1]
                    f.write('Cluster' + str(i) + ':    '+str(index_tuples[0])+'    ')

                    f.write(str(index_tuples[3]) + ' ')
                    f.write('\n')
                    for feeds_id in index_tuples[2]:
                        f.write(feeds_id+'\n')
                    f.write('\n\n')
        '''
if __name__ == '__main__':
    main()
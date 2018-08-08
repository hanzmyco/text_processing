import config
import text_processing.src.read_json as read_json
import Vectorizer
import KMeans
import Algorithm

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

    if config.mode =='Training':

        if config.algo_name =='KMeans':
            algo_instance = KMeans.KMeansClustering(config.algo_name)
            print('start training model')
            algo_instance.fit(model.feature)
            algo_instance.serilize_model()
            algo_instance.get_centroids()
            algo_instance.output_cluster_info(data_in,model,feed_id)

    else:
        if config.algo_name =='KMeans':
            algo_instance = KMeans.KMeansClustering(config.algo_name)
            algo_instance.de_serilize_model()
            algo_instance.get_centroids()
            algo_instance.output_cluster_info(data_in, model, feed_id)


if __name__ == '__main__':
    main()
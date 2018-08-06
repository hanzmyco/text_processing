use_hashing = False
model_name="TfIdf"
path_in="E:\caption_data\subtitle"
stop_word_path="C:\\Users\\mycohzhang\\source\\text_processing\\data\\chinese_stop_words.txt"
algo_name='KMeans'
max_iter=1000
cluster_number=35
top_terms_file="C:\\Users\\mycohzhang\\source\\text_processing\\data\\"+str(cluster_number)+"_clusters_"+str(max_iter)+"_iters_top_terms.txt"
cluster_out_file="C:\\Users\\mycohzhang\\source\\text_processing\\data\\"+str(cluster_number)+"_clusters_"+str(max_iter)+"_iters.txt"
n_features=10000
n_components=False
minibatch=None
verbose=False
data_lines=None
model_file_name="C:\\Users\\mycohzhang\\source\\text_processing\\model\\"+str(cluster_number)+"_clusters_"+str(max_iter)+"_iters.pkl"
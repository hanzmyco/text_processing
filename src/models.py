import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
sys.path.append('..')
import tensorflow as tf
import config


class BaseModel(object):
    def __init__(self, model):
        self.model = model
        self.path = '../data/' + model + '.txt'
        self.temp = tf.constant(1.5)
        self.batch_size = config.BATCH_SIZE
        self.lr = config.LR
        self.skip_step = 1
        self.len_generated = 200
        self.gstep = tf.Variable(0, dtype=tf.int32, trainable=False, name='global_step')
        self.num_classes = config.NUM_CLASSES
        self.out_state = None
        self.in_state = None
        self.sample = None
        self.num_steps = config.NUM_STEPS  # for RNN unrolled, actually use it for cut down
        self.embedding_size = config.EMBEDDING_SIZE
        self.vocab_size=config.VOCAB_SIZE
        self.loss=0

    def create_model(self,one_hot=False,training=True):

        if one_hot:  # not using embedding layer
            embed = self.seq

        else:  # using embedding layer
            with tf.name_scope('embed'):
                if not config.PRETRAIN_EMBD_TAG:
                    embed_matrix = tf.get_variable('embed_matrix',
                                                   shape=[self.vocab_size, self.embedding_size],
                                                   initializer=tf.random_uniform_initializer())

                else:
                    embed_matrix = tf.Variable(self.pretrain_embd,
                                               trainable=config.PRETRAIN_EMBD_TRAINABLE,name='embed_matrix')
                    '''
                    #make sure the pretrain embd is load correctly
                    with tf.Session() as sess:
                        sess.run(tf.initialize_all_variables())
                        print(sess.run(embed_matrix))
                    '''
                embed = tf.nn.embedding_lookup(embed_matrix, self.seq, name='embedding')


                if training:
                    num_clusters = 5
                    kmeans = tf.contrib.factorization.KMeansClustering(
                        num_clusters=num_clusters, use_mini_batch=False)

                    # train
                    num_iterations = 10
                    previous_centers = None
                    for _ in range(num_iterations):
                      kmeans.train(self.input_fn)
                      cluster_centers = kmeans.cluster_centers()
                      if previous_centers is not None:
                        print('delta:'), cluster_centers - previous_centers
                      previous_centers = cluster_centers
                      print('score:'), kmeans.score(self.input_fn)
                    print('cluster centers:'), cluster_centers

                    # map the input points to their clusters
                    cluster_indices = list(kmeans.predict_cluster_index(embed))

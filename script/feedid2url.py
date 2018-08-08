import random
def feedid2url(file_in,file_out,top_k):
    count_cluster=0
    container=[]
    with open(file_out, 'w', encoding='utf-8') as f_out:
        with open(file_in, encoding='utf-8') as f_in:
            text='1'
            while text:
                text=f_in.readline()
                print(text)
                if text.startswith('Cluster'):
                    if len(container) >10:
                        for ite in random.sample(container,10):
                            f_out.write(ite)
                    else:
                        for ite in container:
                            f_out.write(ite)
                    f_out.write('\n')
                    count_cluster += 1
                    if count_cluster>=10000:
                        print('stop')
                    if count_cluster > top_k:
                        return

                    for ite in text.split(' '):
                        f_out.write(ite.strip()+'\t')
                    f_out.write('\n')

                    container=[]
                elif text.strip()!='':
                    container.append('https://h5.qzone.qq.com/weishi/feed?_proxy=1&_wv=1&id='+text)
                    #f_out.write('https://h5.qzone.qq.com/weishi/feed?_proxy=1&_wv=1&id='+text)
        if len(container) > 10:
            for ite in random.sample(container, 10):
                f_out.write(ite)
        else:
            for ite in container:
                f_out.write(ite)


file_in='C:\\Users\\mycohzhang\\source\\text_processing\\data\\5000_clusters_1000_iters_top_terms.txt'
file_out='C:\\Users\\mycohzhang\\source\\text_processing\\data\\annotation\\5000_clusters_1000_iters_top_terms.txt'
top_k=10
feedid2url(file_in,file_out,5000)


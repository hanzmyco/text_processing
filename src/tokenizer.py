import jieba
import jieba.analyse


def tokenize(data_in,data_out):
    with open(data_out,'w',encoding='utf-8') as f:
        for line in open(data_in,encoding='utf-8'):
            line=line.strip()
            seg_list = jieba.cut(line, cut_all=False)
            #segs = [str(word) for word in list(seg_list) if word not in stoplist]
            f.write(' '.join(seg_list)+'\n')


data_in='C:\\Users\\mycohzhang\\source\data\\video_info\\description.txt'
data_out='C:\\Users\\mycohzhang\\source\data\\video_info\\description.txt.tok'

tokenize(data_in,data_out)
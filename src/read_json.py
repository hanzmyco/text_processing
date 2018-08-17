import json
from pprint import pprint
import sys
from pathlib import Path
from pathlib import PureWindowsPath
import jieba
import jieba.analyse


def read_video_info(file_name,data_out,label_out):
    video={}
    #video_xijing={}
    num_xijing = 0
    num_selfie=0
    num_shoushiwu=0

    for line in open(file_name, encoding='utf-8'):
        line = line.strip()
        data = json.loads(line)
        key=data['feedid']

        if data['category']!='' and data['description'].strip()!='':
            class_=data['category'].split(',')
            description = data['description']

            # handle \n\r etc
            filtered_des=description.splitlines()[0]
            if filtered_des=='':
                continue

            if class_[0]== '戏精':
                num_xijing+=1
                video[key] = (filtered_des, 0)
            elif class_[0]=='自拍':
                video[key] = (filtered_des, 1)
                num_selfie+=1
            elif class_==['跳舞','手势舞']:
                video[key] = (filtered_des, 2)
                num_shoushiwu+=1

    print(num_xijing)
    print(num_selfie)
    print(num_shoushiwu)
    print(len(video))

    with open(data_out,'w',encoding = 'utf-8') as f:
        with open(label_out, 'w', encoding='utf-8') as f_label:
            for ite in video:
                f.write(video[ite][0].strip()+'\n')
                f_label.write(str(video[ite][1])+'\n')


def read_json(path_in,data_out,stop_word_path,vid_out=None,set_limit=None,file_out=None):
    p = Path(path_in)
    file_names = list(p.glob('*.txt'))
    print(len(file_names))
    stoplist = set([line.strip() for line in open(stop_word_path,encoding='utf-8')])

    limit=0


    for file_name in file_names:
        file_name = str(file_name)
        with open(file_name, encoding='utf-8') as f:
            data = json.load(f)
            for vid in data:
                if set_limit and limit >set_limit:
                    break
                ite = ''
                for text in data[vid].split('\n'):
                    words = text.strip().split(']')
                    if len(words) > 1 and (words[1] != '\n' or words[1] != '\r'):
                        # print(words[1])
                        for token in words[1]:
                            if token != '' and token != ' ':
                                ite += token
                if vid_out!=None:
                    vid_out.append(vid)

                seg_list = jieba.cut(ite, cut_all=False)
                segs = [str(word) for word in list(seg_list) if word not in stoplist]
                data_out.append(' '.join(segs))

                if set_limit:
                    limit+=1
    print(len(data_out))
    print('stop')


if __name__ == '__main__':
    file_name = 'C:\\Users\\mycohzhang\\source\data\\video_info\\json2.txt'
    data_out = 'C:\\Users\\mycohzhang\\source\data\\video_info\\description.txt'
    label_out = 'C:\\Users\\mycohzhang\\source\data\\video_info\\label.txt'
    read_video_info(file_name, data_out, label_out)




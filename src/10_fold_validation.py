from sklearn.model_selection import train_test_split
# read_in data_total as a file, generate 10 sets of different training and testing sets

def k_fold_validation(data_total,label_total):
    data_all=[]
    label_all=[]

    for line in open(data_total, encoding='utf-8'):
        data_all.append(line.strip())
    for line in open(label_total):
        label_all.append(line.strip())

    # randomly split data and label into 2 sets, one for train, one for test

    for index in range(0,10):
        X_train,X_test,y_train,y_test = train_test_split(data_all,label_all,test_size=0.1)

        with open('C:\\Users\\mycohzhang\\source\\text_classification\\data\\video_info\\10_cross_validation\\train\\train.txt.ids.'+str(index), 'w', encoding='utf-8') as f:
            for ite in X_train:
                f.write(ite+'\n')

        with open('C:\\Users\\mycohzhang\\source\\text_classification\\data\\video_info\\10_cross_validation\\test\\test.txt.ids.'+str(index), 'w', encoding='utf-8') as f:
            for ite in X_test:
                f.write(ite+'\n')

        with open('C:\\Users\\mycohzhang\\source\\text_classification\\data\\video_info\\10_cross_validation\\train\\label.txt.'+str(index), 'w', encoding='utf-8') as f:
            for ite in y_train:
                f.write(ite+'\n')

        with open('C:\\Users\\mycohzhang\\source\\text_classification\\data\\video_info\\10_cross_validation\\test\\label_test.txt.'+str(index), 'w', encoding='utf-8') as f:
            for ite in y_test:
                f.write(ite+'\n')

data_total='C:\\Users\\mycohzhang\\source\\text_classification\\data\\video_info\\train.txt.ids'
label_total='C:\\Users\\mycohzhang\\source\\text_classification\\data\\video_info\\label.txt'
k_fold_validation(data_total,label_total)








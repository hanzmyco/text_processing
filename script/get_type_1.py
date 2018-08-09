def get_type_1(input,output_file):
    output_contain=[]
    with open(output_file,'w+',encoding='utf-8') as f:
        tag=0
        for line in open(input,encoding='utf-8'):
            line=line.strip()
            if not line.startswith('Cluster'):
                if tag:
                    output_contain.append(line)
                continue

            if len(output_contain)!=0:
                for ite in output_contain:
                    f.write(ite+'\n')
                f.write('\n')
                output_contain=[]
            if line.startswith('Cluster1849'):
                break

            tokens=line.split('\t')
            if len(tokens) <2:
                continue

            real_types =[ite for ite in tokens if ite !='']
            real_type=real_types[-2].split('：')[1]
            print(real_type)
            if real_type ==str(1):
                    tag=1
                    f.write(line+'\n')
            else:
                    tag=0

input='C:\\Users\\mycohzhang\\source\\text_clustering\\data\\annotation\\5000_clusters_1000_iters_top_terms_filtered.txt'

output='C:\\Users\\mycohzhang\\source\\text_clustering\\data\\annotation\\5000_clusters_1000_iters_top_terms_filtered_out.txt'

get_type_1(input,output)
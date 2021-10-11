from collections import defaultdict
from sklearn.model_selection import train_test_split
import wget
import gzip

def _rep_white(x):
    return x
    .replace("Biological Process","Biological_Process")
    .replace("Molecular Function","Molecular_Function")
    .replace("Pharmacologic Class","Pharmacologic_Class")
    .replace("Cellular Component","Cellular_Component")
    .replace("Side Effect","Side_Effect")
    
    
if __name__ == "__main__":
    url = 'https://github.com/hetio/hetionet/raw/master/hetnet/tsv/hetionet-v1.0-edges.sif.gz'
    wget.download(url, 'edges.sif.gz')

    with gzip.open('edges.sif.gz', 'rb') as f:
        content = f.read()
    content = [x.strip() for x in content[1:]]

    rel2edges = defaultdict(list)
    for line in content:
        h,r,t = line.split("\t")
        rel2edges[r].append(line)

    trainf = open("train.txt","w")
    testf = open("test.txt","w")
    validf = open("valid.txt","w")

    for relation in rel2edges.keys():
        train, test = train_test_split(rel2edges[relation], test_size=0.05, random_state=42)
        train, valid = train_test_split(train, test_size=0.05, random_state=42)
        for x in train:
            trainf.write(_rep_white(x) + "\n")
        for x in test:
            testf.write(_rep_white(x) + "\n")
        for x in valid:
            validf.write(_rep_white(x) + "\n")

    trainf.close()
    testf.close()
    validf.close()

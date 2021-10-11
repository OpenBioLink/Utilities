from collections import defaultdict
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    url = "https://storage.cloud.google.com/pheknowlator/archived_builds/release_v2.0.0/build_11FEB2021/knowledge_graphs/instance_builds/relations_only/owlnets/PheKnowLator_v2.0.0_full_instance_relationsOnly_OWLNETS.nt"
    wget.download(url, 'edges.nt')
    
    with open("edges.nt") as infile:
        content = infile.readlines()
    content = [x.strip() for x in content[1:]]

    rel2edges = defaultdict(list)
    for line in content:
        h,r,t,_ = line.split(" ")
        rel2edges[r].append(h + "\t" + r + "\t" + t)

    trainf = open("train.txt","w")
    testf = open("test.txt","w")
    validf = open("valid.txt","w")

    for relation in rel2edges.keys():
        if len(rel2edges[relation]) < 3:
            train = rel2edges[relation]
            test = []
            valid = []
        else:
            train, test = train_test_split(rel2edges[relation], test_size=0.05, random_state=42)
            train, valid = train_test_split(train, test_size=0.05, random_state=42)
        for x in train:
            trainf.write(x + "\n")
        for x in test:
            testf.write(x + "\n")
        for x in valid:
            validf.write(x + "\n")

    trainf.close()
    testf.close()
    validf.close()

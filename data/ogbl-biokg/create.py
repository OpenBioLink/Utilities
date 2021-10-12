from ogb.linkproppred import LinkPropPredDataset

dataset = LinkPropPredDataset(name = "ogbl-biokg")
split_edge = dataset.get_edge_split()
train_edge, valid_edge, test_edge = split_edge["train"], split_edge["valid"], split_edge["test"]

print(train_edge["relation"][0])

with open("train.txt", "w") as out:
    for i in range(len(train_edge["head"])):
        out.write(str(train_edge["head_type"][i]) + ":" + str(train_edge["head"][i]) + "\t" + str(train_edge["relation"][i]) + "\t"+ str(train_edge["tail_type"][i]) + ":" + str(train_edge["tail"][i]) + "\n")

with open("test.txt", "w") as out:
    for i in range(len(test_edge["head"])):
        out.write(str(test_edge["head_type"][i]) + ":" + str(test_edge["head"][i]) + "\t" + str(test_edge["relation"][i]) + "\t"+ str(test_edge["tail_type"][i]) + ":" + str(test_edge["tail"][i]) + "\n")

with open("valid.txt", "w") as out:
    for i in range(len(valid_edge["head"])):
        out.write(str(valid_edge["head_type"][i]) + ":" + str(valid_edge["head"][i]) + "\t" + str(valid_edge["relation"][i]) + "\t"+ str(valid_edge["tail_type"][i]) + ":" + str(valid_edge["tail"][i]) + "\n")
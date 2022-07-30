from collections import Counter
import os
import json
import sys

lang = sys.argv[1].lower()
year = sys.argv[2]

path = f"disambiguated_corpora/{lang.lower()}"
dict_ = {}

for file_name in os.listdir(path):
    
    #customize this according to how you would like to cluster time periods
    if file_name[:file_name.rfind('.')] != year:
        continue

    with open(path+'/'+file_name) as fr:
        data = json.load(fr)
        annotations = data['wsd_annotations']
        for annotation_list in annotations:
            for list_ in annotation_list:
                lemma = list_["lemma"]
                pos = list_["pos"]
                synset = list_["bnSynsetId"]
                if synset == "O":
                    continue
                lemma_pos = lemma + "_" + pos
                dict_.setdefault(lemma_pos, Counter())[synset] += 1

for k,v in dict_.items():
    print(f"{k}", end="\t")
    l = []
    for k_,v_ in v.items():
        l.append(f"{k_} {v_}")
    l = sorted(l, key=lambda x:int(x.split(' ')[1]), reverse=True)
    for idx, item in enumerate(l):
        if idx < len(v)-1:
            print(f"{item}", end="\t")
        else:
            print(f"{item}")



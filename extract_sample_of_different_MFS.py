import os
import json
import sys

def load(paths:list):
    """
    Input: list of distributions (path) to be compared
    Output: Dictionaries containing the distributions
    """
    distributions = {}
    for path in paths:
        distributions[path] = {}
        with open(path, 'r') as fr:
            for line in fr:
                lemma_pos, *meanings = line.strip().split('\t')
                distributions[path][lemma_pos] = meanings
    return distributions

def load_lemmas_pos():
    """
    Input: path to file containing the list of all
    lemmas and their parts of speech present in the
    disambiguated corpora in the following format:
    vivemen_ADJ
    phraorte_NOUN
    Output: a list containing all lemmas and their
    part of speech
    """
    global lemmas_pos
    with open("file_containing_lemmas.txt") as fr:
        for line in fr:
            lemmas_pos.append(line.strip())
    return lemmas_pos

def find_differences(distributions:dict):
    """
    Input: a dictionary containing all distributions
    Output: a file highlighting variations in MFS across
    the considered time periods
    """
    global lemmas_pos, bn2defs, lang
    for lemma_pos in lemmas_pos:
        results = {}
        for d in distributions:
            if lemma_pos in distributions[d]:
                if lemma_pos not in lemmas:
                    continue
                results[d] = distributions[d][lemma_pos]
                previous_meaning = distributions[d][lemma_pos][0].split(' ')[0]
        
        variation = False
        for d, meanings in results.items():
            current_meaning = meanings[0].split(' ')[0]
            if previous_meaning != current_meaning and not variation:
                variation = True
        
        if variation:
            print(f"{lemma_pos}\tDIFFERENT MFS!")
        else:
            #keep this continue to print only the variations in MFS
            #across the considered time periods
            continue
            print(lemma_pos)
        
        final_results, final_results_defs = [], []
        for d, meanings_ in results.items():
            meanings = "\t".join(meanings_)
            final_results.append(f"{d[d.rfind('/')+1:]}\t{meanings}")
            final_results_defs.append(f"{meanings_[0].split(' ')[0]}\t{bn2defs[meanings_[0].split(' ')[0]]}")
        for f in final_results:
            print(f)
        print()
        for f in final_results_defs:
            print(f)
        print()

def load_definitions():
    """
    Loads all BabelNet defintions for the available synsets
    To download BabelNet please register at: https://babelnet.org/login
    and place a tsv file called bn_data.tsv containing the definitions in this format
    bn:00039438n [tab] Type genus of the Ranidae 
    """
    global bn2defs
    with open(f"bn_data.tsv") as fr:
        for line in fr:
            bn, *defs = line.strip().split('\t')
            bn2defs[bn] = defs[0]

def load_inventory():
    """
    Loads BabelNet inventories and applies a filtering
    To download BabelNet please register at: https://babelnet.org/login
    """
    global lemmas
    for file_name in os.listdir("bn_inventory"):
        if f".{lang}." not in file_name: 
            continue
        with open("bn_inventory/"+file_name) as fr:
            for line in fr:
                lemma = line[:line.rfind("#")]
                pos = line[line.rfind("#")+1:line.find("\t")]
                lemmas.add(lemma+"_"+pos)

if __name__ == "__main__":
    
    lang = sys.argv[1]
    #specify the distributions to be analyzed as in this example
    #distributions = load(["distributions/sl/sl_1600.tsv", "distributions/sl/sl_1700.tsv", "distributions/sl/sl_1800.tsv", "distributions/sl/sl_1900.tsv"])
    #distributions = 

    bn2defs, lemmas_pos = {}, []
    lemmas = set()
    load_lemmas_pos()
    load_inventory()
    load_definitions()
    find_differences(distributions)


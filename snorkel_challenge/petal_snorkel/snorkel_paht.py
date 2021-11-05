import pandas as pd 
from snorkel.labeling import LabelingFunction
import itertools
import math
from snorkel.labeling.lf.core import labeling_function

'''
    Useful Functions 
'''
def keyword_lookup(x,bio_functions:pd.DataFrame,bio_function_rules:pd.DataFrame):
    """Returns the id corresponding to the label

    Args:
        x (str): some phrase

    Returns:
        int: the id
    """
    for i in range(len(bio_functions)):
        label_name = bio_functions.iloc[i]['function'] 
        label_id = bio_functions.iloc[i]['function_enumerated']        
        
        label_rule_name = label_name + "_rules"
        if label_rule_name in list(bio_function_rules.columns):
            phrases_to_look_for = bio_function_rules[label_rule_name].to_list()
            phrases_to_look_for = [x for x in phrases_to_look_for if x == 'nan']
            for phrase in phrases_to_look_for:
                # now you could make a counter and see the percentage match so if 10/20 phrases are in the text/abstract then you return the
                if phrase in x.text.lower():     
                    return label_id 
    return -1

'''
    Main Code 
'''


def create_labeling_functions(bio_file:pd.DataFrame, bio_rules:pd.DataFrame):
    """create a list of labeling functions

    Args:
        bio_file (pd.DataFrame): a list of all the biomimicry functions
        bio_rules (pd.DataFrame): a list of all the 'rules' for each biomimicry function

    Returns:
        labeling_function_list: a list of all the labeling function 'rules' corresponding to each biomimicry function
    """
    bio_file = pd.read_csv(bio_file)
    bio_rules = pd.read_csv(bio_rules)

    lst = []
    underscore_list = []
    rules_no_na = []
    labeling_function_list = []
    
    #get a list of all the rules
    for i in range(len(bio_file)):
        label_name = bio_file.iloc[i]['function'] 
        label_rule_name = label_name + "_rules"
        if label_rule_name in list(bio_rules.columns):
            phrases_lst = bio_rules[label_rule_name].to_list()
            lst.append(phrases_lst)
    chained_lst = (list(itertools.chain.from_iterable(lst)))
    #remove blank cells
    remove_na = [x for x in chained_lst if pd.isnull(x) == False]
    #remove duplicates
    for rule in remove_na:
        if rule not in rules_no_na:
            rules_no_na.append(rule)
    #add underscore to rules
    for item in rules_no_na:
        item = item.replace(" ", "_")
        underscore_list.append(item)
    #create labeling function for each rule
    for phrase in underscore_list:
        labeling_function = LabelingFunction(name=f"keyword_{phrase}", f=keyword_lookup,
                        resources={"bio_functions":bio_file,"bio_function_rules":bio_rules})
        labeling_function_list.append(labeling_function)

    # print(len(labeling_function_list))
    return labeling_function_list
    


# create_labeling_functions(r'C:\Users\ARalevski\Documents\petal_snorkel\biomimicry_functions_enumerated.csv', r'C:\Users\ARalevski\Documents\petal_snorkel\biomimicry_function_rules.csv')



        
##goal is to grab the key of the first dictonary and then all the keys that are related to the orginial key


import json
import pandas as pd
import samplePaths
def get_data(file):
    openData = open(file, "r")        
    data = json.load(openData)     
    result = []
    valHolder = []
    for keys, values in data.items():
        currResult = {}
        currResult[samplePaths.keyVal()] = keys
        for inner_key, inner_val in values.items():
            valHolder.append(inner_key) 
        currResult[samplePaths.valueVal()] = valHolder
        result.append(currResult)
        valHolder = []
    return result

def export_data(data):     ###convert them to a csv
    df = pd.DataFrame(data)
    df.to_csv(samplePaths.outputPath())

def execute():###run the program 
    data = get_data(samplePaths.inputPath())
    export_data(data)
    
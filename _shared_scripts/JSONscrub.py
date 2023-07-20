import json
import pandas as pd
import paths
def get_data(file):
    openData = open(file, "r")
    data = json.load(openData)
    result = []
    valHolder = []
    for keys, values in data.items():
        currResult = {}
        currResult[paths.keyVal()] = keys
        for inner_key, inner_val in values.items():
            valHolder.append(inner_key) 
        currResult[paths.valueVal()] = valHolder
        result.append(currResult)
        valHolder = []
    return result

def export_data(data):
    df = pd.DataFrame(data)
    df.to_csv(paths.outputPath())

def execute():
    data = get_data(paths.inputPath())
    export_data(data)
    
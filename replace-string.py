import json
import pandas as pd

data_file = "data.json"
rows = pd.read_excel('test_sample.xlsx')

old_str = list(rows["Old"])
new_str = list(rows["New"])
old_new_pairs = list(zip(old_str, new_str))

with open(data_file, 'r') as f:
    strf = f.read()

def replace_from_json(data, replace_values):
    new_data = data
    for i in replace_values:
        new_data = new_data.replace(i[0], i[1])
    with open(data_file, 'w') as f:
        json.dump(json.loads(new_data), f, indent=4)
        
replace_from_json(strf, old_new_pairs)

# github desktop test
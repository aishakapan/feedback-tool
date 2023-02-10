import json

data_file = "data.json"

with open(data_file) as f:
    data = json.load(f)


def replace_from_json(data, old_str, new_str):
    stringified_data = str(data)
    updated = stringified_data.replace(old_str, new_str)
    double_quote_updated = updated.replace("'", '"')
    updated_json = json.loads(double_quote_updated)
    return updated_json
    
def write_into_json():
    pass

old_str = "Look here's some text I wanna replace cause it sucks."
new_str = "Shiny new sentence."

replace_from_json(data, old_str, new_str)
print(data)
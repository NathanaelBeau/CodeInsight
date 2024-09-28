import pandas as pd

def test(lst0):
    data = []
    for item in lst0:
        flat_dict = {}
        for key, value in item.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    flat_dict[f"{key}.{sub_key}"] = sub_value
            else:
                flat_dict[key] = value
        data.append(flat_dict)
    return pd.DataFrame(data)
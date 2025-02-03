import pandas as pd
import json
from pandas import json_normalize

# Load JSON file into DataFrame
with open('test_3.json', 'r') as file:
    json_data = file.read()
    
parsed_data = json.loads(json_data)

# Normalize JSON data into a DataFrame
df = pd.json_normalize(parsed_data)

df.to_csv('output1.csv', index=True)
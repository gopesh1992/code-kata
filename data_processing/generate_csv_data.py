import pandas as pd

data = {
    'first_name': ['John', 'Jane'],
    'last_name': ['Doe', 'Smith'],
    'address': ['123 Elm St', '456 Oak St'],
    'date_of_birth': ['1980-01-01', '1990-02-02']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

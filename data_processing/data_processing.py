import pandas as pd
import dask.dataframe as dd
import hashlib

def anonymize(value):
    return hashlib.md5(value.encode()).hexdigest()

def process_csv(input_file, output_file):
    df = dd.read_csv(input_file, assume_missing=True)
    df['first_name'] = df['first_name'].map(anonymize, meta=('x', 'str'))
    df['last_name'] = df['last_name'].map(anonymize, meta=('x', 'str'))
    df['address'] = df['address'].map(anonymize, meta=('x', 'str'))
    df.to_csv(output_file, index=False, single_file=True)

process_csv('data.csv', 'anonymized_data.csv')

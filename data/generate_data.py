import numpy as np
import pandas as pd

def generate_data(rows=1000000):
    data = {
        'A': np.random.randint(0, 100, size=rows),
        'B': np.random.randint(0, 100, size=rows),
        'C': np.random.rand(rows)
    }
    return data

def save_data_files():
    data = generate_data()
    df = pd.DataFrame(data)
    df.to_csv('data/test_data.csv', index=False)
    df.to_parquet('data/test_data.parquet', index=False)
    df.to_json('data/test_data.json', orient='records', lines=True)

if __name__ == "__main__":
    save_data_files()
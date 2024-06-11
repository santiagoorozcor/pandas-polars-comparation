import pandas as pd
import polars as pl
from helpers.performance import memory_usage

def benchmark_selection():
    df_pandas = pd.read_csv('data/test_data.csv')
    df_polars = pl.read_csv('data/test_data.csv')

    # Pandas column selection
    mem_usage_pandas, exec_time_pandas, _ = memory_usage(lambda: df_pandas['A'])

    # Polars column selection
    mem_usage_polars, exec_time_polars, _ = memory_usage(lambda: df_polars['A'])

    print(f"Pandas column selection memory usage: {mem_usage_pandas:.2f} MB, execution time: {exec_time_pandas:.4f} seconds")
    print(f"Polars column selection memory usage: {mem_usage_polars:.2f} MB, execution time: {exec_time_polars:.4f} seconds")

if __name__ == "__main__":
    benchmark_selection()
import pandas as pd
import polars as pl
from helpers.performance import memory_usage


def benchmark_loading():
    # Pandas loading CSV
    mem_usage_pandas_csv, exec_time_pandas_csv, _ = memory_usage(pd.read_csv, 'data/test_data.csv')

    # Polars loading CSV
    mem_usage_polars_csv, exec_time_polars_csv, _ = memory_usage(pl.read_csv, 'data/test_data.csv')

    print(f"Pandas CSV loading memory usage: {mem_usage_pandas_csv:.2f} MB, execution time: {exec_time_pandas_csv:.4f} seconds")
    print(f"Polars CSV loading memory usage: {mem_usage_polars_csv:.2f} MB, execution time: {exec_time_polars_csv:.4f} seconds")

def main():
    benchmark_loading()

if __name__ == "__main__":
    main()
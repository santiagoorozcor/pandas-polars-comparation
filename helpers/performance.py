import os
import time
import psutil
from typing import Callable, Tuple, Any


def memory_usage(func: Callable, *args, **kwargs) -> Tuple[float, float, Any]:
    """
    Measure the memory usage and execution time of a given function.

    Parameters:
        func (callable): The function to be measured.
        *args: Variable length argument list for the function.
        **kwargs: Arbitrary keyword arguments for the function.

    Returns:
        tuple: A tuple containing memory usage in MB, execution time in seconds, and the function's result.
    """
    process = psutil.Process(os.getpid())

    # Measure memory before execution
    mem_before = process.memory_info().rss / 1024 / 1024  # Convert bytes to MB

    start_time = time.time()

    try:
        result = func(*args, **kwargs)
    except Exception as e:
        raise RuntimeError(f"Error executing function {func.__name__}: {e}")
    
    end_time = time.time()

    # Measure memory after execution
    mem_after = process.memory_info().rss / 1024 / 1024  # Convert bytes to MB

    mem_usage = mem_after - mem_before
    exec_time = end_time - start_time

    return mem_usage, exec_time, result

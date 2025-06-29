from prefect import flow, task
import numpy as np
from pathlib import Path


@task
def compute_stats(numbers: list[float]) -> tuple[float, float]:
    arr = np.array(numbers)
    return arr.mean(), arr.std()

@flow(log_prints=True, name="Hello Numpy Flow")
def hello_numpy_flow():
    # basic math
    nums = [1, 2, 3, 4, 5]
    mean, std = compute_stats(nums)
    print(f"Computed over {nums!r}: mean={mean:.2f}, std={std:.2f}")

    for entry in Path('/share').iterdir():
        if entry.is_file():
            print(f"File: {entry.name}")

if __name__ == "__main__":
    hello_numpy_flow()

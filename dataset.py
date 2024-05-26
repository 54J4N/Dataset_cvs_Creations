import pandas as pd
import numpy as np

def generate_data(num_records, chunk_size=100000):
    """
    Generate a dataset and save it in chunks to a CSV file.
    
    Args:
    num_records (int): Total number of records to generate.
    chunk_size (int): Number of records per chunk.
    """
    columns = ['ID', 'Feature1', 'Feature2', 'Feature3', 'Label']
    file_path = 'large_dataset.csv'

    pd.DataFrame(columns=columns).to_csv(file_path, index=False)

    for start in range(0, num_records, chunk_size):

        end = min(start + chunk_size, num_records)
        data = {
            'ID': np.arange(start + 1, end + 1),
            'Feature1': np.random.uniform(0, 1, end - start),
            'Feature2': np.random.uniform(0, 1, end - start),
            'Feature3': np.random.uniform(0, 1, end - start),
            'Label': np.random.randint(0, 2, end - start)
        }
        df = pd.DataFrame(data)
        
        df.to_csv(file_path, mode='a', header=False, index=False)

if __name__ == '__main__':
    generate_data(1000000)  # Adjust the number here for more records

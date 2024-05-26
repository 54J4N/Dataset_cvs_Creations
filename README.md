# Large Dataset Generator

This Python script generates a large dataset and saves it to a CSV file in chunks. It is designed to handle the creation of datasets with potentially millions of records without overwhelming memory resources.

## Description

The script uses the Pandas and NumPy libraries to generate a dataset with specified features and labels. It saves the data in chunks to ensure efficiency and manageability for large datasets.

## Features

- Generate a customizable number of records.
- Save the dataset in chunks for efficient memory management.
- Automatically label data for potential use in machine learning training.

## Requirements

- Python 3.x
- Pandas
- NumPy

Install the required packages using pip:

```bash
pip install pandas numpy

Usage
To run the script and generate data, you can specify the number of records you want to generate. 
For example, to generate 1,000,000 records:

python <script_name>.py
You can adjust the num_records parameter in the script to change the number of records generated.

Configuration
num_records: Total number of records to generate (default is 1,000,000).
chunk_size: Number of records per chunk (default is 100,000).
Output
The script outputs a CSV file named large_dataset.csv containing the following columns:

ID
Feature1
Feature2
Feature3
Label

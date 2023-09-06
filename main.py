"""Main function goes here"""
import pandas as pd


def describe_file(input1):
    """define a function read a file"""
    df1 = pd.read_csv(input1)
    return df1.describe()

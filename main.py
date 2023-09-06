"""Main function goes here"""
import pandas as pd


def func(input1):
    """define a function read a file"""
    penguins = pd.read_csv(input1)
    return penguins

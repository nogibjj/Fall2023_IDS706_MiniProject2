"""
Test Cases
"""
from main import func


def test_read():
    """test function"""
    print(
        func("https://github.com/allisonhorst/palmerpenguins/blob/main/data/penguins.R")
    )

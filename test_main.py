"""
Test Cases
"""
from main import describe_file


def test_read():
    """test function"""
    df1 = describe_file("https://www.dropbox.com/s/x2awp0e9znsyub7/egrid2016.csv?dl=1")
    assert df1["SEQPLT16"]["mean"] == 4855.0
    assert df1["SEQPLT16"]["count"] == 9709.0
    assert df1["CAPFAC"]["count"] == 8038.0

if __name__ == "__main__":
    test_read()

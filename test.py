import unittest
from logging.config import fileConfig


class TestLoggingConfig(unittest.TestCase):
    def test_case0(self):
        fileConfig("case0.ini")

    def test_case1(self):
        fileConfig("case1.ini")

    def test_case2(self):
        fileConfig("case2.ini")

    def test_case3(self):
        fileConfig("case3.ini")


if __name__ == "__main__":
    unittest.main()

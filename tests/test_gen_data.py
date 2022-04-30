import unittest
import pandas as pd
from src.gen_data import *

class testGenData(unittest.TestCase):

    def test_gen(self):
        test_name = "tests/test_generated_data.csv"
        gen_data(1, test_name)
        df = pd.read_csv(test_name)
        self.assertEqual(len(df), 1)


if __name__ == '__main__':
    unittest.main()

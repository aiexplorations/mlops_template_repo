import unittest
import pandas as pd
from src.gen_data import *

class testGenData(unittest.TestCase):

    def test_gen(self):
        gen_data(1)
        df = pd.read_csv("data.csv")
        self.assertEqual(len(df), 1)


if __name__ == '__main__':
    unittest.main()

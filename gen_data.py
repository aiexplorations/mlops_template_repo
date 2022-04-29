import numpy as np
import pandas as pd

n = 1000

df = pd.DataFrame({"x1":np.random.normal(10,1,n), "x2": np.random.normal(20,2,n)})

df.to_csv("data.csv")

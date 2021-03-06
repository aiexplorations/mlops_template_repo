import numpy as np
import pandas as pd
import logging

n = 1000

def gen_data(n, file_name):
    if n >= 1:
        non_zero_neg = n >= 1
       
        if non_zero_neg:
            
            df = pd.DataFrame({"x1":np.random.normal(10,1,n), "x2": np.random.normal(20,2,n)})
            df['y'] = np.random.normal(0,1,n) + 2*df['x1'] + 3*df['x2']

            df.to_csv(file_name)

            logging.log(logging.INFO,'Created data.csv with '+str(n)+' records,')
            
        
    else:
            
        logging.error(logging.ERROR, "n should be greater than or equal to 1")
        raise Exception("n should be greater than or equal to 1")

gen_data(n, "data.csv")

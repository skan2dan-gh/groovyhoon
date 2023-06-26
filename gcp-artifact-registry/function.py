
import pandas as pd
import numpy as np
import sys

def create_quantile_df(): 

    # Create an empty dataframe with columns as cts_cols and index as quantiles
    quantile_df=pd.DataFrame(columns=['quantile'], data=[0.1,0.25,0.5,0.75,0.8,0.9,0.95,0.97,0.99], index=np.arange(1, 10, dtype=int))

    return quantile_df


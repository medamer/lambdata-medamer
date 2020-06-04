

from my_lambdata.my_mod import Data
import pandas as pd
import numpy as np


df= pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'))

profile = Data.profile
split = Data.split

print(profile(df))

print(split(df))
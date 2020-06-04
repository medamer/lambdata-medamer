

from my_lambdata.my_mod import Data
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/medamer/Datasets/master/oasis_longitudinal.csv')

data = Data()

print(data.profile(df))
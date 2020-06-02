# Import libraries:
import pandas as pd
#from scikit-learn.model_selection import train_test_split
"""
# function to clean te dataset:
def test(x):
    print(x*10)

"""
def profile(df):
    # Check and print missing values:
    nans = df.isnull().sum()
    nans = pd.DataFrame(nans, columns=['NaNs'])
    print('Missing Values :')
    
    #Describe dataset:
    print('\n')
    print('Describe dataset', df.describe().T)

    # Make the train/test split:
    #train, test = train_test_split(df, test_size=0.2, stratify=df['Group'], random_state=42)
    #train, val = train_test_split(train, train_size=0.8, test_size=0.2, stratify=train['Group'], random_state=42)
    #print('\n')
    #print('Train shape     : ', train.shape)
    #print('Validation shape: ', val.shape)
    #print('Test shape      : ', test.shape)
    print('\n')
    print(df.head())

# Import libraries:
import pandas as pd
from scikit-learn.model_selection import train_test_split


class Data:
    # function to clean te dataset:
    def profile(df):

        """
        Param df is dataframe
        Function checks for NaNs, print them, and print the description.
        """
        nans = df.isnull().sum()
        nans = pd.DataFrame(nans, columns=['NaNs'])

        # Check and print missing values:
        print('Missing Values : \n', nans)

        # Describe dataset:

        print('\n')
        print('Describe dataset : \n', df.describe().T)

    def split(df):
        # Make the train/test split:
        """
        Param df is dataframe.
        Function split the dataframe into train, validation and test.
        """
        train, test = train_test_split(
                                        df, test_size=0.2,
                                        stratify=df['Group'],
                                        random_state=42
                                        )
        train, validation = train_test_split(
                                                train, train_size=0.8,
                                                test_size=0.2,
                                                stratify=train['Group'],
                                                random_state=42
                                                )
        print('\n')
        print('Train shape     : ', train.shape)
        print('Validation shape: ', validation.shape)
        print('Test shape      : ', test.shape)
import pandas as pd

def extract_data():

    features_df = pd.read_csv(r'C:\Users\ALL AtoZ\Downloads\retail_project\data\Features_dataset.csv')
    sales_df = pd.read_csv(r'C:\Users\ALL AtoZ\Downloads\retail_project\data\sales_dataset.csv')
    store_df = pd.read_csv(r'C:\Users\ALL AtoZ\Downloads\retail_project\data\stores_dataset.csv')

    print('Features Dataset')
    print(features_df.head())
    print(features_df.dtypes)

    print('Sales Dataset')
    print(sales_df.head())
    print(sales_df.dtypes)

    print('Store Dataset')
    print(store_df.head())
    print(store_df.dtypes)

    return features_df, sales_df, store_df
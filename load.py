from sqlalchemy import create_engine

def load_data(fact_sales, dim_store, dim_date, dim_feature):

    db_name = 'retail_project'
    db_host = 'localhost'
    db_port = 5432
    db_pass = 'your password'
    db_user = 'postgres'

    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

    dim_store.to_sql('dim_store',
                     engine,
                     schema= 'public',
                     if_exists = 'replace',
                     index = False)
    
    dim_date.to_sql('dim_date',
                     engine,
                     schema= 'public',
                     if_exists = 'replace',
                     index = False)
    
    dim_feature.to_sql('dim_feature',
                     engine,
                     schema= 'public',
                     if_exists = 'replace',
                     index = False)
    
    fact_sales.to_sql('fact_sales',
                     engine,
                     schema= 'public',
                     if_exists = 'replace',
                     index = False)
    
    print('Data loaded to postges successfully')
from sqlalchemy import create_engine,MetaData
import urllib


params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};'
                                 'SERVER=172.16.3.94;'
                                 'DATABASE=registrobilletes;'
                                 'UID=ramiro;'
                                 'PWD=quirogon')
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

meta=MetaData()

# To test the connection
conn= engine.connect() 



# engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
import pyodbc
import pandas
import numpy
import json

configfile = 'SQLServerConfig'

json_file = open(configfile)

data = json.load(json_file)

ConnectionString = F"Driver={data['SQLServer']['Driver']}" \
                   F";Server={data['SQLServer']['Server']}" \
                   F";Database={data['SQLServer']['Database']}" \
                   F";Trusted_Connection={data['SQLServer']['Trusted_Connection']}"
print(ConnectionString)

def header(x):
    return print(f'[{x}]')


def f_conn():
    return pyodbc.connect(ConnectionString)


pd = pandas
conn = f_conn()

pd.set_option('display.max_columns',500)
pd.set_option('display.max_rows',500)
pd.set_option('display.width',1000)

query = ('select  sh.SalesOrderNumber'
        ', sh.OrderDate'
        ', DueDate'
        ', ShipDate'
        ', Status'
        ', sh.SubTotal'
        ', sh.TaxAmt'
        ', sh.Freight'
        ', ProductID'
        ', UnitPrice'
        ', sd.OrderQty '
        'from Sales.SalesOrderHeader sh '
        'inner join Sales.SalesOrderDetail sd '
        'on sh.SalesOrderID = sd.SalesOrderID')

result = pd.read_sql(query, conn)

header('3.result type')
print(result.dtypes)

header('4. result.values')
print (result.values)

header('5. result.describe()')
print(result.describe())

header('6. select single column')
print(result.loc[1:100,['ProductID','OrderDate','UnitPrice','OrderQty']])

import pandas
pd = pandas

file_path = 'C:\\Users\\Benjamin\\source\\repos\\Data Source\\Transaction_Product.csv'
pd.set_option('display.max_columns',100)
pd.set_option('display.width',1000)
df = pd.read_csv(file_path)

print(df.head(10))

num = 0

def pt (a):
    global num
    num = num + 1
    print (f'\n{num}. [{a}] \n')

pt('Add Compute Column and Drop the Column')

df['Tax Override Cost'] = df['ActualCost']/1.1

print (df.head(2))

pt ('Drop Column')
df = df.drop(columns=['Tax Override Cost'])
print (df.head(2))

pt('Compute Column with Aggregate Function')
df['ActualCost+ListPrice'] = df.iloc[:,[1,6]].sum(axis=1)
print(df.head(100))
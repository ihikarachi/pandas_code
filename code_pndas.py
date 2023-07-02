import pandas as pd

df = pd.read_csv('test.csv')
# print (df)
# print (df.head())
# print (df.head(2))
# print (df.tail(1))
# for i in df:  # for all columns detail
#     print(i) #print(df[i])
# print (df['Name'])
# print (df[['Name','Salary']])
# print (df['Age']+df['Salary'])
# print (df['Name'][2])
# print (df.shape)
# x = df[['Name','Age']]
# print (x.shape)

# print (df['Depart'] == 'HR')
# print (df[df['Depart'] == 'HR'])
# print (df[ (df['Depart'] == 'HR') | (df['Depart'] == 'IT') ])
# print (df[ (df['Depart'] == 'HR') & (df['Salary'] > 5000) ])
# print (df['Depart'].isin(['HR','IT']))
# print (df['Age'].notna())
# print (df[ df['Age'].notna() ])

# print (df['Salary'].sum())
# print (df['Salary'].max())
# print (df['Salary'].min())
# print (df['Salary'].mean())
# print (df['Age'].median())
# print (df['Salary'].describe())

# print ( df['Name'].str.len() )
# print ( df['Name'].str.upper() )
# print ( df['Name'].str.lower() )
# print ( df['Name'].str.contains ('S') )
# print ( df['Name'].str.contains ('S') )
# print (df['Name'].str.split (':'))
# x = df['Name'].replace ({'Saleem':'Kareem' , 'Arif': 'Atif'})
# print(x)
# x = df.sort_values(['Depart','Name'],ascending=False)
# print (x)

# dx = pd.DataFrame (
#     {
#         'Name' : ['test','s',None,'asd'],
#         'Age' : [3,4,5,6]
#     }
# )

# print(dx)
# dx.to_csv('new.csv')

# itm = {'Name':'New Data', 'Age' : 50}
# df = df.append(itm,ignore_index=True)
# print(df)

# pip install matplotlib

from matplotlib import pyplot as plt

# df = df.sort_values('Age')
# x = df['Age'] #[10,20,50,40]
# y = df ['Name'] #['A','B','C','D']
# plt.plot (x,y)
# plt.xlabel ('sssssssss')
# plt.show()
# plt.plot (x,y,'o')
# plt.show()


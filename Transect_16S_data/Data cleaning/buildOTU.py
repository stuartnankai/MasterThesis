import pandas as pd

df = pd.read_table('../Training Data/Data_all_2016_otus.txt', delim_whitespace=True, index_col=0)
# print("This is : ", data)
# print("This is the size of data: ", df.shape)

# df['Bacteria'] = df['Taxonomy'].str.extract('([A-Z]\w{0,})', expand=True)
# print("This is : ", df['Bacteria'])

taxnonmy1 = []
taxnonmy2 = []
taxnonmy3 = []
taxnonmy4 = []
taxnonmy5 = []
taxnonmy6 = []

# For each row in a varible,
for row in df['Taxonomy']:
    # Split the row by comma and append
    # everything before the comma to lat
    taxnonmy1.append(row.split(';')[0])
    # Split the row by comma and append
    # everything after the comma to lon
    taxnonmy2.append(row.split(';')[1])
    taxnonmy3.append(row.split(';')[2])
    taxnonmy4.append(row.split(';')[3])
    taxnonmy5.append(row.split(';')[4])
    taxnonmy6.append(row.split(';')[5])

# Create two new columns from lat and lon
df['taxnonmy1'] = taxnonmy1
df['taxnonmy2'] = taxnonmy2
df['taxnonmy3'] = taxnonmy3
df['taxnonmy4'] = taxnonmy4
df['taxnonmy5'] = taxnonmy5
df['taxnonmy6'] = taxnonmy6


del df['Taxonomy']
cols = df.columns.tolist()
# cols = cols[-1:-6] + cols[:-6]

cols = cols[-6:]+cols[:-6]

df = df[cols]

# print df

"File generated already"
# writer = pd.ExcelWriter('../Training Data/mergeOTU_split.xlsx')
#
# df.to_excel(writer, 'sheet1')
#
# writer.save()

for j in range(1,7):

    numUnclass = df['taxnonmy%d'%j].value_counts()
    print("This is the name of subclass: ", numUnclass )
    print("This is subclass of texnonmy: ", len(numUnclass))
    print("########################")

import pandas as pd

"""

list1 = ['H', 'e', 'l', 'l', 'o']

se = pd.Series(list1)
print(se)

print("value with index:", se[0])

print("_"*10)
se1 = pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'])
print(se1)

print("value with index:", se1['b'])


print("value with index:", se[0])

print("_"*10)
se2 = pd.Series(2.01, index=['a', 'b'])
print(se2)

########################### Create serise with ###############
print("_"*30)
dict1 = {'name': 'Pratik', 'job': 'Data Analyst', 'Salary': 100000}

dict_se = pd.Series(dict1)

print(dict_se)

print(dict_se.index)
print(dict_se.shape, "size :",  dict_se.size, "data type :",  dict_se.dtype, "value :", dict_se.values)

"""

#####################################################################################

data = {'name' : ['ram', 'pratik', 'altaf'], 'job' : ['QA', 'Developer', 'Analyst'] }

frame = pd.DataFrame(data)

print(frame)

print("_"*40)

shope_data = {'Fruit Name' : ['apple', 'mango', 'banana'], 'Price' : [50, 100, 40], 'Quantity' : [10, 5, 10],
              'Fruit Bill' : [500, 500, 400]}

shope_frame = pd.DataFrame(shope_data)
print(shope_frame)
print("Total Bill Payment :", sum(shope_data['Fruit Bill']))


########################### Create data Fram with List data ####################
print("_"*40)
list1 = ['apple', 'mango', 'banana', 'Lichi', 'pinapple']

df = pd.DataFrame(list1)

#print(df)

list2 = [['apple', 'mango', 'banana', 'Lichi', 'pinapple'], [50, 40, 20, 60, 80], [10, 20, 30, 5, 1], [10, 30, 40]]

df2 = pd.DataFrame(list2, index=['name', 'price', 'quantity', 'bill'])

print(df2)

########################### Create data frame with Series ###################
print("_"*40)

list1 = [4, 6, 8, 9, 7]
list2 = [7, 22, 8, 12, 44, 55]
list3 = [6, 22, 44, 12, 34, 88]

se1 = pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'])
se2 = pd.Series(list2, index=['a', 'b', 'c', 'd', 'e', 'f'])
se3 = pd.Series(list3, index=['a', 'b', 'c', 'd', 'e', 'f'])

df_series = pd.DataFrame({'first' : se1, 'second' : se2})

print(df_series)
print("_"*40)

df_series['three'] = se3

print(df_series)

############### Delete colom1 ###########
print("_"*40)

del df_series['first']

print(df_series)
print("_"*40)

print(df_series['second']['c'])

df_series['second']['c'] = 50

print("_"*40)

print(df_series)

print("_"*40)
# remove colom with pop

output = df_series.pop('second')

print(output)
print("_"*40)
print(df_series)








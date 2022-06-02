import pandas as pd
"""
info = {'name' : ['rushi', 'ram', 'pratik', 'dipak', 'altaf'],
        'job' : ['devloper', 'Analyst', 'data engineer', 'QA', 'Admin'],
        'salary' : [10000, 5000, 40000, 30000, 100000]}

df = pd.DataFrame(info)

print(df)

csv_data = df.to_csv()
print("_"*40)
print(csv_data)


######################### Read data from csv ####################

print("_"*40)
csv_data = pd.read_csv('users_data.csv')

print(csv_data)
print("_"*40)
print(csv_data['Name'])


######################################################

info = {'name' : ['rushi', 'ram', 'pratik', 'dipak', 'altaf'],
        'job' : ['devloper', 'Analyst', 'data engineer', 'QA', 'Admin'],
        'salary' : [10000, 5000, 40000, 30000, 100000]}

df = pd.DataFrame(info,  index=[4, 5, 2, 3, 1])

print(df)
########################################## sort the dataframe data ################
print("#"*30)
sort_data = df.sort_index()
print(sort_data)

print("#"*30)
sort_data2 = df.sort_index(ascending=False)
print(sort_data2)

print("#"*30)
sort_data3 = df.sort_values('name')
print(sort_data3)

print("#"*30)
sort_data4 = df.sort_values('salary')
print(sort_data4)

##################### sum of the data ################
print("#"*30)
sum_of_all_salary = sort_data4['salary'].sum()
print("total salary :", sum_of_all_salary)

"""
############################## Concatenation of Data frame #####################


info1 = {'name' : ['rushi', 'ram', 'pratik', 'dipak', 'altaf'],
        'job' : ['devloper', 'Analyst', 'data engineer', 'QA', 'Admin'],
        'salary' : [10000, 5000, 40000, 30000, 100000],
         'bonus' : [2000, 1000, 3000, 500, 4000]}

info2 = {'name' : ['john', 'jany', 'jaggu', 'jasus', 'janardan'],
        'job' : ['sale', 'marketing', 'recention', 'mechanic', 'accout'],
        'salary' : [10000, 15000, 12000, 450000, 30000],
        'bonus' : [2500, 1010, 3300, 5500, 4400]}



df1 = pd.DataFrame(info1)
df2 = pd.DataFrame(info2)

output = df1.append(df2, ignore_index=True)

print(output)

salary = output['salary'].sum()
print("salary :", salary)
print("#"*40)

payments = []

for i in range(10):
    payments.append(output['salary'][i]+output['bonus'][i])


output['payments'] = payments
print("#"*40)
print(output)


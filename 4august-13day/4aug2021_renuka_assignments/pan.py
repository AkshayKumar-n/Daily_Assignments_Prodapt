import pandas
d=pandas.read_csv('student.csv')
print(d.describe())
print(d['name'])         #print(d.name)
print(d.head(n=2))       #prints default 5
print(d.tail(n=2))
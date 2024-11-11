import pandas as pd

data=pd.read_csv("books.csv",usecols=["Price"])
"""Skipping Rows:
data=pd.read_csv(books.csv,skiprows=44,nrows=2)
"""

print(data)

maxiumum=data.max()
print(maxiumum)
minimum=data.min()
print(minimum)

"""Shivam is analyzing the top 50 books sold on amazon. He is having data in the form of the CSV file
( books.csv ). Create a series of the price column and find the price of the book on row 20."""
print("*********************************************")
data=pd.read_csv("books.csv",usecols=["Price"])
print(data.loc[20,["Price"]])

#Changing price
data=pd.read_csv("books.csv",usecols=["Price"])
update=data.loc[30,["Price"]]=55
print(update)
print("*********************************************")

master=pd.read_csv("books.csv",usecols=["UserRating"])
print(master)

t1=pd.DataFrame(master,index=[20])
print(t1)
"""
Renaming a column:
resut=pd.DataFrame(data,index=['first','second])
print(result)
u=result.rename(index={'first':'FIRST','second':'SECOND'})
print(u)"""

#Just Revewing
goat=pd.DataFrame(master,index=[76])
print(goat)
new=data.loc[23,["UserRating"]]=4.9
print(new)
new1=data.loc[23,["UserRating"]]
print(new1)

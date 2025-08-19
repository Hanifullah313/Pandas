import pandas as pd
#merging two data frames
"""
there are 5 functions to merge() methods data frames in pandas:
 1.inner
   inner for merging data frames on common columns and returning only the rows with matching values.
 2.outer
   outer for merging data frames on common columns and returning all rows, with NaN for missing values.
 3.left
   left for merging data frames on common columns and returning all rows from the left DataFrame.
 4.right
   right for merging data frames on common columns and returning all rows from the right DataFrame.
 5.cross
   cross for merging data frames and returning the Cartesian product of the rows.
"""
data1 ={
    "name": ["John", "Anna", "Peter"],
    "age": [28, 24, 35]
}
data2 = {
    "name": ["John", "Anna", "Peter" ,  "kashif"],
    "city": ["New York", "Paris", "Berlin", "London"]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged = pd.merge(df1, df2, on="name" , how="inner")
print(f'Merged DataFrame:\n{merged}')
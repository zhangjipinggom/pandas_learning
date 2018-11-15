import pandas as pd
import numpy as np
import functools

# review what learned yesterday
# the main knowledge is about how to sort datafram and select it by multi-critia

df = pd.read_excel("examples.xls")
df_sort = df.loc[df.学号.argsort()]  # sort the datafram

# select the datafram by multi-critia
Crit1 = df.该班入学年月 == '2014-09-01'
Crit2 = df.培养层次码_显示值 == "硕士"
Crit3 = df.学习形式代码 == 1
CritList = [Crit1, Crit2, Crit3]
df_select = df.loc[functools.reduce(lambda x, y: x & y, CritList)]
df_select.to_excel("example.new.xls")

# learn how to use the function lambda
List = np.array([1, 2, 3])
a = functools.reduce(lambda x, y: -x+y, List)
a = lambda x, y: -List    # this is a function
print(a(1, 1)) # you have to give a parameter


# learn something today
# Selecting
# Selecting according to both the index and column value
# method 1
df = pd.DataFrame( {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
df_select = df[(df.AAA > 4) & (df.index.isin([0, 3]))]
print(df_select)



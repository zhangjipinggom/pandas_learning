import functools

import pandas as pd
import numpy as np

df = pd.read_excel("examples.xls")
# review what learned yesterday
df["level"] = np.where(df.年级 <= 2013, "old", "new")
df.to_excel("example_new.xls")

# spliting
# select the index satisfy some condition
df_new = df.loc[df.年级 > 2013]

# Building Criteria
# 选择满足多个条件的行， 这其实也是昨天的内容
df_new = df[(df.年级 == 2013) & (df.是否在职生 == 0)]
# 根据条件修改某列
df.loc[(df.年级 == 2013) | (df.学习形式代码 == 1), "注册状态"] = 1
# 根据条件增加某列
df["满足条件"] = np.where((df.年级 == 2013) | (df.学习形式代码 == 1), "是", "否")


# 根据条件进行排序
df2 = pd.DataFrame({'AAA': [4,5,6,7], 'BBB': [10,20,30,40], 'CCC': [100,50,-30,-50]})
df2_sort = df2.loc[(df2.AAA-5.5).abs().argsort()]
df2_sort2 = df2.loc[(df2.AAA-5.5).argsort()]
a = df2.AAA  # 这得到的是一个Series
print(df2_sort2)

# 多个条件选择
Crit1 = df2.AAA <= 5.5
Crit2 = df2.BBB == 10
Crit3 = df2.CCC > -40.0
CritList = [Crit1, Crit2, Crit3]
AllCrit = functools.reduce(lambda x, y: x & y, CritList)   # reduce： x&y&z
print(df2.loc[AllCrit])



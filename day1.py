import pandas as pd
import numpy as np

# 这样能实现一个if-then-else-then的功能，根据某一列的信息修改特定列
# 方法1：
df = pd.DataFrame({"AAA": np.arange(1, 5), "BBB": np.random.rand(4),   # 只能写4， 不能写（4,1）
                   "CCC": np.random.gamma(shape=2, scale=1, size=4)})  # 前两个参数是控制gamma函数的性质的，size是输出的shape
df.loc[df.AAA > 2, "BBB"] = 0
df.loc[df.AAA <= 2, "BBB"] = 1
print(df)

# 方法2
# 修改特定列的另一种方法： datafram中的where，但这需要一个mask
df_mask = pd.DataFrame({"AAA": [True]*4, "BBB": [False]*4, "CCC": [True, False]*2})
df_mask2 = pd.DataFrame({"CCC": [True, False]*2})
df2 = df.where(cond=df_mask, other=2)  # 如果值为True, 保留原来的值， False, 用后面的值替代
df3 = df.where(cond=df_mask2, other=2)  # 仅改变指定列
print(df3)


# 方法3
# 结合numpy中的where
df["logic"] = np.where(df["AAA"] > 2, "high", "low")   # 新增加一列，满足条件则取x, 否则取y
df["BBB"] = np.where(df["AAA"] > 2, "high", "low")   # 修改原来的列
print(df)
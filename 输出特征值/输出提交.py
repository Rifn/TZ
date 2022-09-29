import pandas as pd


df1 = pd.read_csv("../02_traits_tz.csv")
df2 = pd.read_csv("../02_traits_yz.csv")
df3 = pd.read_csv("../02_traits_needtest.csv")

df1.to_excel("./TZ_同指_Traits.xlsx", index=False)
df2.to_excel("./TZ_异指_Traits.xlsx", index=False)
df3.to_excel("./TZ_同异合并_Traits.xlsx", index=False)

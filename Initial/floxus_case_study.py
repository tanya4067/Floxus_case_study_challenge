import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel(r'C:\Users\tanya\Downloads\ipl.xlsx')
df['SOLD PRICE'].diff().hist() #histogram for sold price
# box plot to find the outliers
table_numeric_features=df.select_dtypes(include=[np.number])
table_numeric_features.columns
#table_numeric_features.corr()
#table_numeric_features.boxplot(column=['PLAYING ROLE','T-RUNS','T-WKTS','ODI-RUNS-S','ODI-SR-B','ODI-WKTS','ODI-SR-BL','CAPTAINCY EXP','RUNS-S','HS','AVE','SR-B','SIXERS','RUNS-C','WKTS','AVE-BL','ECON','SR-BL','AUCTION YEAR'])#
#table_numeric_features.boxplot()
#plt.show()
Q1=table_numeric_features.quantile(0.25)
Q3=table_numeric_features.quantile(0.75)
IQR=Q3-Q1
print(IQR)
df_final=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]
df_final.shape

# scatter_plot

#ax=df.plot.scatter(x="SIXERS",y="SOLD PRICE",color="DarkBlue")
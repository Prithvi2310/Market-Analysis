import pandas as pd

#converting xls to csv
data = pd.read_excel("NSE_Listings_MarketCap")
data.drop(['Sr. No.'],axis=1,inplace=True)
data.to_csv("NSE_Listings_MarketCap.csv",index=False)
print(data.columns)
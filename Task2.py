import pandas as pd

df=pd.read_excel("miuul_gezinomi.xlsx")

'''
# if there is no "SaleCheckInDayDiff
df["CheckInDate"]=pd.to_datetime([df["CheckInDate"]])
df["SaleDate"]=pd.to_datetime([df["SaleDate"]])
df["SaleCheckDate"]=df["CheckInDate"]- df["SaleDate"]
'''
# 2
# SaleCheckInDayDiff=CheckInDate-SaleDate
def assign_eb_score(row):
    if row<=7:
        return "Last Minuters"
    elif row>7 & row<=30:
        return "Potential Planners"
    elif row>30 & row<=90:
         return "Planners"
    elif row>90:
         return "Early Brookers"

df["EB_Score"]=df["SaleCheckInDayDiff"].apply(assign_eb_score)

print(df["EB_Score"])
print(df["EB_Score"].value_counts())
print(df.head(50))
import pandas as pd
df=pd.read_excel("miuul_gezinomi.xlsx")

# 3
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

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

agg_df=df.groupby(["SaleCityName","ConceptName","EB_Score"]).agg({"Price":["mean","count"]})
print(agg_df)

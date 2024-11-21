import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

df=pd.read_excel("miuul_gezinomi.xlsx")
# sales_level_based
# SaleCityName ConceptName Seasons Price---- sales_level_based
# sales_level_based  row=SaleCityName+ConceptName+Seasons
def assign_eb_score(row):
        if row <= 7:
            return "Last Minuters"
        elif 7 < row <= 30:
            return "Potential Planners"
        elif 30 < row <= 90:
            return "Planners"
        elif row > 90:
            return "Early Brookers"


df["EB_Score"]=df["SaleCheckInDayDiff"].apply(assign_eb_score)

agg_df=df.groupby(["SaleCityName","ConceptName","EB_Score","Seasons","Price"]).agg({"Price":["mean","count"]})

# multi index
agg_df.columns=['_'.join(col).strip() if isinstance(col,tuple) else col for col in agg_df.columns]
# 5
agg_df.reset_index(inplace=True)

# 6
def assign_sales_level(col1, col2, col3):
    return f"{col1}_{col2}_{col3}".upper()

agg_df["sales_level_based"]=agg_df.apply(lambda row: assign_sales_level(row["SaleCityName"],row["ConceptName"],row["Seasons"]),
                                         axis=1)


# 7

agg_df["Segment"]=pd.qcut(agg_df["Price_mean"],4, labels=["D","C","B","A"])

segment_summary=agg_df.groupby("Segment").agg({"Price_mean": ["mean","max","sum"]})


#8
# print(agg_df["sales_level_based"].unique())

new_user="ANTALYA_HERŞEY DAHIL_HIGH"

cost=agg_df[agg_df["sales_level_based"]==new_user]["Price_mean"].mean()
print(f"cost of ANTALYA_HERŞEY DAHIL_HIGH: {cost}")

new_user2="GIRNE_YARIM PANSIYON_LOW"
segment2=agg_df[agg_df["sales_level_based"]==new_user2]["Segment"].values[0]
print(f"segment of GİRNE_YARIM PANSIYON_LOW: {segment2}")
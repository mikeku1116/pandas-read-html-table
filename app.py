import pandas as pd


bus_table = pd.read_html("https://www.ubus.com.tw/Booking/FareInquiry")

bus_df = bus_table[0]
bus_df.columns = ["路線名稱", "優惠時段", "原價時段", "半票票價", "軍優票價", "去回票價"]
print(bus_df)

print("===========================================")

product_table = pd.read_html(
    "https://web.elifemall.com.tw/allnewweb/product.php?idept=100&showlist=&isdept=120")

df = pd.DataFrame()
for index in range(1, len(product_table), 2):
    product_df = product_table[index].T  # 轉置表格
    df = pd.concat([df, product_df], ignore_index=True)  # 合併DataFrame

df.columns = ["name", "model", "price"]  # 自訂欄位名稱
df = df.groupby("name").first()  # 以名稱來進行群組
print(df)

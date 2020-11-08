import pandas as pd


bus_table = pd.read_html("https://www.ubus.com.tw/Booking/FareInquiry")

bus_df = bus_table[0]
bus_df.columns = ["路線名稱", "優惠時段", "原價時段", "半票票價", "軍優票價", "去回票價"]
print(bus_df)

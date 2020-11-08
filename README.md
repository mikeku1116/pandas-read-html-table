# pandas-read-html-table #

## 專案介紹 ##

本專案利用Pandas套件的read_html()方法(Method)，讀取[統聯客運乘車票價表](https://www.ubus.com.tw/Booking/FareInquiry)及[全國電子冰箱價格](https://www.ubus.com.tw/Booking/FareInquiry)的網頁表格資料，除此之外，取得的冰箱價格資料使用Pandas套件的表格轉置及群組(Groupby)技巧，提升資料的可讀性，可以搭配[[Pandas教學]掌握Pandas DataFrame讀取網頁表格的實作技巧](https://www.learncodewithmike.com/2020/11/read-html-table-using-pandas.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境：

`$ pipenv shell`

登入後，就能夠執行app.py範例程式。
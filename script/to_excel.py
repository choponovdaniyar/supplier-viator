#pandas, bs4
import pandas
from bs4 import BeautifulSoup


def get_data(fpath = ".data/result.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        #lxml
        #openpyxl
        html = BeautifulSoup(f.read(), "lxml")

    result = {
        "product_id": list(),
        "title": list(),
        "status": list()
    }

    items = html.find_all("li", class_="ProductListItem__productListItem___284B3 ProductListItem__productListItemNewLayout___3A7_l")
    for item in items:
        id = item.find("span", class_="ProductListItem__productCodeContainer___3CDcP").text
        title = item.find("div", class_="ProductListItem__productTitle___1DAk7").find("strong").text
        status = item.ind("div", class_="ProductListItemStatus__status___3BWpM ProductListItem__productListItemStatus___O5zNw").text
        result["product_id"].append(id)
        result["title"].append(title)
        result["status"].append(status)

    return  result

def to_excel():
    df = pandas.DataFrame(get_data)
    df.to_excel(".\data\result.xlsx")




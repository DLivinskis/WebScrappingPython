from bs4 import BeautifulSoup  # to parse HTML data
import requests  # to get HTML data
import xlsxwriter  # to save scrapped data to the excel spreadsheet
from datetime import date  # to get today's date which will be used in naming of the file
import re  # to get rid of text in price column

today = date.today()
print("Today's date:", today)

products = {"lg+c1+48", "lg+c1+55", "lg+c1+65", "lg+c1+77", "lg+c1+83", "lg+c2+42", "lg+c2+48", "lg+c2+55", "lg+c2+65",
            "lg+c2+77", "lg+c1+83", "samsung+qn90a+43", "samsung+qn90a+50", "samsung+qn90a+65", "samsung+qn90a+75",
            "samsung+qn90a+85"}
row = 1
column = 0
column1 = 1
column2 = 2
column3 = 3
thislistNames = []
thislistPrices = []


for product in products:
    url = f"https://www.salidzini.lv/cena?q={product}"
    response = requests.get(url)
    page = response.text

    # print(webpage.text)
    soup = BeautifulSoup(page, 'html.parser')
    names = soup.findAll("h2", class_="item_name")
    # results = soup.find("div", class_="item_box_main")
    # print(results)

    for name in names:
        # print(name.text.strip(), end="\n"*2)
        # a = str(name.text.strip())
        nameAsText = str(name.text.strip())
        thislistNames.append(nameAsText)


    prices = soup.findAll("div", class_="item_price")
    for price in prices:
        # print(price.text.strip(),end="\n"*2)
        PriceAsText = str(price.text.strip())
        PriceAsText = PriceAsText.split(".")
        PriceAsText = re.sub("[^0-9]", "", PriceAsText[0])
        thislistNames.append(PriceAsText)

print(thislistNames)
print(thislistPrices)


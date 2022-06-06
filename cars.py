from bs4 import BeautifulSoup
import urllib
import lxml.html as LH
import requests
import pandas as pd
import time
import io
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')
brand_list = ['Alfa-Romeo','Cadillac','Chevrolet','Chrysler','Citroen','Dacia','Dodge','Fiat','Ford','Honda','Hyundai','Infiniti','Jaguar','Jeep','Kia','Lancia','Land-Rover','Lexus','Mazda','Mini','Mitsubishi','Nissan','Opel','Peugeot','Porsche','Renault','Saab','Seat','Skoda','Smart','Subaru','Suzuki','Toyota']
biggest_brands = ['Audi','BMW','Mercedes','Volkswagen','Volvo']


url = 'https://www.ss.com/en/transport/cars/Alfa-Romeo/page1.html'
r = requests.get(url)
root = LH.fromstring(r.content)
for table in root.xpath('//*[@id="filter_frm"]/table[2]'):
    header = ['Select', 'Key', 'Ad', 'Model','Year','Volume','Mileage','Price']        # 1
    data = [[text(td) for td in tr.xpath('td')]
      for tr in table.xpath('//tr')]                   # 2
    data = [row for row in data if len(row)==len(header)]    # 3
    data = pd.DataFrame(data, columns=header)
    data['date'] = pd.to_datetime('today')
    data['Brand'] = 'Alfa-Romeo'
    page = urllib.request.urlopen('https://www.ss.com/en/transport/cars/Alfa-Romeo/page1.html')
    soup = BeautifulSoup(page,'html.parser')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    images = list(filter(lambda k: 'gallery' in k, images))
    imagesdf = pd.DataFrame (images, columns = ['Key'])
    data = data.drop('Key', axis=1)
    data = data.drop('Select', axis=1)
    data = pd.concat([data, imagesdf],axis=1)

for y in brand_list:
    url = 'https://www.ss.com/en/transport/cars/'+y+'/page1.html'
    r = requests.get(url)
    root = LH.fromstring(r.content)
    for table in root.xpath('//*[@id="filter_frm"]/table[2]'):
        header = ['Select', 'Key', 'Ad', 'Model','Year','Volume','Mileage','Price']        # 1
        data1 = [[text(td) for td in tr.xpath('td')]
                for tr in table.xpath('//tr')]                   # 2
        data1 = [row for row in data1 if len(row)==len(header)]    # 3
        data1 = pd.DataFrame(data1, columns=header)
        data1['date'] = pd.to_datetime('today')
        data1['Brand'] = y
        page = urllib.request.urlopen('https://www.ss.com/en/transport/cars/'+y+'/page1.html')
        soup = BeautifulSoup(page,'html.parser')
        images = []
        for img in soup.findAll('img'):
            images.append(img.get('src'))
        images = list(filter(lambda k: 'gallery' in k, images))
        imagesdf = pd.DataFrame (images, columns = ['Key'])
        data1 = data1.drop('Key', axis=1)
        data1 = data1.drop('Select', axis=1)
        data1 = pd.concat([data1, imagesdf],axis=1)
        data=pd.concat([data,data1], ignore_index=True)

    for x in range(50):
        url = 'https://www.ss.com/en/transport/cars/' + y + '/page'+str(x)+'.html'
        r = requests.get(url)
        root = LH.fromstring(r.content)
        for table in root.xpath('//*[@id="filter_frm"]/table[2]'):
            header = ['Select', 'Key', 'Ad', 'Model', 'Year', 'Volume', 'Mileage', 'Price']  # 1
            data2 = [[text(td) for td in tr.xpath('td')]
                    for tr in table.xpath('//tr')]  # 2
            data2 = [row for row in data2 if len(row) == len(header)]  # 3
            data2 = pd.DataFrame(data2, columns=header)  # 4
            data2['date'] = pd.to_datetime('today')
            data2['Brand'] = y  
            page = urllib.request.urlopen('https://www.ss.com/en/transport/cars/'+y+'/page'+str(x)+'.html')
            soup = BeautifulSoup(page,'html.parser')
            images = []
            for img in soup.findAll('img'):
                images.append(img.get('src'))
            images = list(filter(lambda k: 'gallery' in k, images))
            imagesdf = pd.DataFrame (images, columns = ['Key'])
            data2 = data2.drop('Key', axis=1)
            data2 = data2.drop('Select', axis=1)
            data2 = pd.concat([data2, imagesdf],axis=1)
            data2['page'] = x
            data=pd.concat([data,data2], ignore_index=True)

for j in biggest_brands:
    url = 'https://www.ss.com/en/transport/cars/'+j+'/page1.html'
    r = requests.get(url)
    root = LH.fromstring(r.content)
    for table in root.xpath('//*[@id="filter_frm"]/table[2]'):
        header = ['Select', 'Key', 'Ad', 'Model','Year','Volume','Mileage','Price']        # 1
        data3 = [[text(td) for td in tr.xpath('td')]
                for tr in table.xpath('//tr')]                   # 2
        data3 = [row for row in data3 if len(row)==len(header)]    # 3
        data3 = pd.DataFrame(data3, columns=header)
        data3['date'] = pd.to_datetime('today')
        data3['Brand'] = j
        page = urllib.request.urlopen('https://www.ss.com/en/transport/cars/'+j+'/page1.html')
        soup = BeautifulSoup(page,'html.parser')
        images = []
        for img in soup.findAll('img'):
            images.append(img.get('src'))
        images = list(filter(lambda k: 'gallery' in k, images))
        imagesdf = pd.DataFrame (images, columns = ['Key'])
        data3 = data3.drop('Key', axis=1)
        data3 = data3.drop('Select', axis=1)
        data3 = pd.concat([data3, imagesdf],axis=1)
        data=pd.concat([data,data3], ignore_index=True)

    for i in range(110):
        url = 'https://www.ss.com/en/transport/cars/' + j + '/page'+str(i)+'.html'
        r = requests.get(url)
        root = LH.fromstring(r.content)
        for table in root.xpath('//*[@id="filter_frm"]/table[2]'):
            header = ['Select', 'Key', 'Ad', 'Model', 'Year', 'Volume', 'Mileage', 'Price']  # 1
            data4 = [[text(td) for td in tr.xpath('td')]
                    for tr in table.xpath('//tr')]  # 2
            data4 = [row for row in data4 if len(row) == len(header)]  # 3
            data4 = pd.DataFrame(data4, columns=header)  # 4
            data4['date'] = pd.to_datetime('today')
            data4['Brand'] = j
            page = urllib.request.urlopen('https://www.ss.com/en/transport/cars/'+j+'/page'+str(i)+'.html')
            soup = BeautifulSoup(page,'html.parser')
            images = []
            for img in soup.findAll('img'):
                images.append(img.get('src'))
            images = list(filter(lambda k: 'gallery' in k, images))
            imagesdf = pd.DataFrame (images, columns = ['Key'])
            data4 = data4.drop('Key', axis=1)
            data4 = data4.drop('Select', axis=1)
            data4 = pd.concat([data4, imagesdf],axis=1)
            data4['page'] = i
            data=pd.concat([data,data4], ignore_index=True)
            print(data)

data = data.drop_duplicates(subset=['Key'], keep='first')

TodaysDate = time.strftime("%Y-%m-%d")
excelfilename = TodaysDate +".xlsx"

connect_str = os.getenv('DefaultEndpointsProtocol=https;AccountName=phantomssdata;AccountKey=DofyxRt8JJqTpcn/GLMr6SicN6oJtdAukdvkRffzgqa1UsBDcn0VG11Wi9b7cIn5N1cwTfWPePVY+AStALKjag==;EndpointSuffix=core.windows.net')
blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=phantomssdata;AccountKey=DofyxRt8JJqTpcn/GLMr6SicN6oJtdAukdvkRffzgqa1UsBDcn0VG11Wi9b7cIn5N1cwTfWPePVY+AStALKjag==;EndpointSuffix=core.windows.net')
local_path = "./"

data.to_excel(excelfilename ,index = False)
upload_file_path = os.path.join(local_path, excelfilename)
blob_client = blob_service_client.get_blob_client(container='cars', blob=excelfilename)
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
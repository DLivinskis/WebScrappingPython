from bs4 import BeautifulSoup #to parse HTML data
import os
import shutil
import requests #to get HTML data
import xlsxwriter #to save scrapped data to the excel spreadsheet
from datetime import date #to get today's date which will be used in naming of the file
import re #to get rid of text in price column
from time import sleep

today = date.today()
current_path = str(os.getcwd()) + "\\" + str(today) + ".xlsx"

def Get_Number_Of_Job_Ads(): #Function that goes to CV.LV and finds the number of Job ads currently. Each day there is different number
    url = 'https://cv.lv/lv/search?limit=20&offset=0&fuzzy=true&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=false&isQuickApply=false'
    response = requests.get(url)


    soup = BeautifulSoup(response.text,'html.parser')

    names = soup.find("span", class_='jsx-1871295890 jsx-2661613696')
    Number_of_results_with_text = (names.get_text())
    Number_of_results = Number_of_results_with_text[22:26]
    return Number_of_results

# Number_Of_Jobs_CV_LV = Get_Number_Of_Job_Ads()
Number_Of_Jobs_CV_LV = 10
def Get_All_Job_Ads(Number_Of_Jobs_CV_LV):
    url =f"https://cv.lv/lv/search?limit={Number_Of_Jobs_CV_LV}&fuzzy=true&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=false&isQuickApply=false"
    response=requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    names = soup.find_all("a",class_=['jsx-586146153 vacancy-item__title',"jsx-586146153"])

    for name in names:
        print(name)
        # print(name.get("jsx-586146153 vacancy-item__title"))
        # print(name.get("href"))
Get_All_Job_Ads(Number_Of_Jobs_CV_LV)

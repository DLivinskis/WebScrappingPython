from bs4 import BeautifulSoup #to parse HTML data
import os
import pandas as pd
import numpy as np
import shutil
import requests #to get HTML data
import xlsxwriter #to save scrapped data to the excel spreadsheet
from datetime import date #to get today's date which will be used in naming of the file
import re #to get rid of text in price column
from time import sleep

today = date.today()
nameOfWorkbook = str(today)+".xlsx"
current_path = str(os.getcwd()) + "\\" + str(today) + ".xlsx"

def Get_Number_Of_Job_Ads(): #Function that goes to CV.LV and finds the number of Job ads currently. Each day there is different number
    url = 'https://cv.lv/lv/search?limit=20&offset=0&fuzzy=true&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=false&isQuickApply=false'
    response = requests.get(url)


    soup = BeautifulSoup(response.text,'html.parser')

    names = soup.find("span", class_='jsx-1871295890 jsx-2661613696')
    Number_of_results_with_text = (names.get_text())
    Number_of_results = Number_of_results_with_text[22:26]
    print(Number_of_results)
    return Number_of_results

# Number_Of_Jobs_CV_LV = Get_Number_Of_Job_Ads()
Number_Of_Jobs_CV_LV = Get_Number_Of_Job_Ads()
print(Number_Of_Jobs_CV_LV)
def Get_All_Job_Ads(Number_Of_Jobs_CV_LV):
    url =f"https://cv.lv/lv/search?limit={Number_Of_Jobs_CV_LV}&fuzzy=true&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=false&isQuickApply=false"
    response=requests.get(url)
    job_title_list = []
    job_company_list = []
    job_link_list = []
    soup = BeautifulSoup(response.text, 'html.parser')
    job_title = soup.find_all(class_="jsx-586146153 vacancy-item__title")
    hiring_company = soup.find_all("a", class_="jsx-586146153")


    for name in hiring_company[::2]:
        job_title_list.append(name.text)
    for name in job_title:
        job_company_list.append(name.text)
    final_list = [job_title_list,job_company_list,job_link_list]
    for name in hiring_company[::2]:
        second_part_of_the_link = name.get('href')
        full_link = 'https://cv.lv' + second_part_of_the_link
        job_link_list.append(full_link)
    return final_list



final_list = Get_All_Job_Ads(Number_Of_Jobs_CV_LV)
df = pd.DataFrame(final_list)
df = df.transpose()
df.columns = ["Location",'Title','Link']
df.insert(loc=3,
               column='Date',
               value=today)

df.to_excel(nameOfWorkbook)
shutil.move(current_path,f'W:\Coding\PythonProjects\ScrappedData\OneDrive\Jobs')
print("Data is extracted succesfully!")

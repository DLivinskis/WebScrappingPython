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
nameOfWorkbook = "3DMark Score per GPU"+".xlsx"
current_path = str(os.getcwd()) + "\\" + nameOfWorkbook


def Get_GPU_Scores():
    url ='https://benchmarks.ul.com/compare/best-gpus?amount=0&sortBy=SCORE&reverseOrder=true&types=MOBILE,DESKTOP&minRating=0'
    response=requests.get(url)
    GPU_Name_List = []
    GPU_Score_List = []
    final_list = []
    soup = BeautifulSoup(response.text, 'html.parser')
    GPU_Name = soup.find_all('a',class_='OneLinkNoTx')
    GPU_Score = soup.find_all(class_="bar-score")


    for name in GPU_Name:
        GPU_Name_List.append(name.text)
    for name in GPU_Score[::2]:
        GPU_Score_List.append(name.text)
    final_list = [GPU_Name_List,GPU_Score_List]
    return final_list



final_list = Get_GPU_Scores()
df = pd.DataFrame(final_list)
df = df.transpose()
df.columns = ["GPU",'Score']


df.to_excel(nameOfWorkbook)
try:
    shutil.move(current_path,f'W:\Coding\PythonProjects\ScrappedData\OneDrive\Salidzini_scrapping\GPU Scores')
    print("Data is extracted succesfully!")
    input()
except:
    print("Something went wrong")
    input()


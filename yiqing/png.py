# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from selenium import webdriver
import pandas as pd

url = "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1"
rank = webdriver.Chrome("chromedriver.exe")
rank.get(url)

country = rank.find_elements_by_class_name("overseas_list_name")
newconfirm = rank.find_elements_by_class_name("overseas_list_today_confirm ")
allconfirm = rank.find_elements_by_class_name("overseas_list_confirm")
dead = rank.find_elements_by_class_name("overseas_list_dead")
heal = rank.find_elements_by_class_name("overseas_list_heal")

countryList = []
newconfirmList = []
allconfirmList = []
deadList = []
healList = []
for i in range(1, 10):
    countryList.append(str(country[i].text))
    newconfirmList.append(newconfirm[i].text)
    allconfirmList.append(int(allconfirm[i].text))
    deadList.append(int(dead[i].text))
    healList.append(int(heal[i].text))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.title
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))



autolabel(plt.bar(range(len(allconfirmList)), allconfirmList, color='rgb', tick_label=countryList))
plt.show()
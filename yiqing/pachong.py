# coding:utf-8
from selenium import webdriver
import datetime
import pandas as pd



def get_data(url):
    rank = webdriver.Chrome("chromedriver.exe")
    rank.get(url)
    time = datetime.datetime.today().strftime('%Y-%m-%d')
    print("截止到"+time)

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
    for i in range(1, len(country)):
        countryList.append(country[i].text)
        newconfirmList.append(newconfirm[i].text)
        allconfirmList.append(allconfirm[i].text)
        deadList.append(dead[i].text)
        healList.append(heal[i].text)

    dict = {
        '国家': countryList,
        '新增确诊': newconfirmList,
        '累计确诊': allconfirmList,
        '死亡': deadList,
        '治愈': healList
    }

    df = pd.DataFrame(dict)
    print(df.all)
    df[["累计确诊"]] = df[["累计确诊"]].astype(int)
    df.to_csv('data.csv',encoding='utf-8_sig')
    return df


def ShowRank(data):
    pd.set_option('display.max_rows', None)
    print(data.all)

def AddRank(data):

    country = input("国家：")
    newconfirm = input("新增确诊：")
    allconfirm = int(input("累计确诊："))
    dead = input("死亡：")
    heal = input("治愈：")
    data.loc[data.shape[0]] = {"国家": country, '新增确诊': newconfirm, '累计确诊': allconfirm, '死亡': dead, '治愈': heal}
    data= data.sort_values('累计确诊', ascending=False)
    data = data.reset_index(drop=True)
    print(data.all)
    print('添加成功')
    data.to_csv('data.csv', encoding='utf-8_sig')
    return data

def DeleteRank(data):
    delet = CheckRank(data)
    data = data.drop(index=data[data['国家'] == delet].index[0])
    data = data.reset_index(drop=True)
    data.to_csv('data.csv', encoding='utf-8_sig')
    return data


def ModifyRank(data):
    index = CheckRank(data)
    target = input('你要修改的属性为：')
    newIndex = input('你要更改为：')
    lastIndex = data.loc[data['国家'] == index, [target]]
    print(lastIndex)
    data.loc[data['国家'] == index, [target]] = newIndex
    print(data.loc[data["国家"] == index])
    print('修改成功')
    data.to_csv('data.csv', encoding='utf-8_sig')
    return data


def CheckRank(data):
    index = input("请输入你要寻找的国家：")
    print(data.loc[data["国家"] == index])
    return index



def main():
    url = "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1"
    data = get_data(url)
    i = 3
    while (i):
        print("""
           排名系统
           1.查看排名表
           2.增
           3.删
           4.改
           5.查
           6.退出
           """)
        choice = input('请选择：')
        if choice == '1':
            ShowRank(data)
        elif choice == '2':
            data = AddRank(data)
        elif choice == '3':
            data = DeleteRank(data)
        elif choice == '4':
            data = ModifyRank(data)
        elif choice == '5':
            CheckRank(data)
        elif choice == '6':
            print('欢迎下次使用')
            exit()
        else:
            print('请输入正确选择')
            i = i - 1
            continue


main()

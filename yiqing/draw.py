from pyecharts import options as opts
from pyecharts.charts import Map


# coding:utf-8
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
for i in range(1, len(country)):
    countryList.append(country[i].text)
    newconfirmList.append(newconfirm[i].text)
    allconfirmList.append(int(allconfirm[i].text))
    deadList.append(int(dead[i].text))
    healList.append(int(heal[i].text))

dict = {
    '国家': countryList,
    '新增确诊': newconfirmList,
    '累计确诊': allconfirmList,
    '死亡': deadList,
    '治愈': healList
}

data = pd.DataFrame(dict)
#ata[["累计确诊"]] = data[["累计确诊"]].astype(int)
data["新增确诊"].apply(lambda x: x.replace('-','0')).astype(int)
print(data["新增确诊"].dtypes)
#data[["新增确诊"]] = data[["新增确诊"]].astype(int)
#data[["死亡"]] = data[["死亡"]].astype(int)
#data[["治疗"]] = data[["治疗"]].astype(int)

data_list_new = list(zip(countryList,newconfirm))
data_list_all = list(zip(countryList,allconfirmList))
data_list_dead = list(zip(countryList,deadList))
data_list_heal = list(zip(countryList,healList))



nameMap ={
  "Somalia": "索马里",
  "Liechtenstein": "列支敦士登",
  "Morocco": "摩洛哥",
  "W. Sahara": "西撒哈拉",
  "Serbia": "塞尔维亚",
  "Afghanistan": "阿富汗",
  "Angola": "安哥拉",
  "Albania": "阿尔巴尼亚",
  "Andorra": "安道尔共和国",
  "United Arab Emirates": "阿拉伯联合酋长国",
  "Argentina": "阿根廷",
  "Armenia": "亚美尼亚",
  "Australia": "澳大利亚",
  "Austria": "奥地利",
  "Azerbaijan": "阿塞拜疆",
  "Burundi": "布隆迪",
  "Belgium": "比利时",
  "Benin": "贝宁",
  "Burkina Faso": "布基纳法索",
  "Bangladesh": "孟加拉国",
  "Bulgaria": "保加利亚",
  "Bahrain": "巴林",
  "Bahamas": "巴哈马",
  "Bosnia and Herz.": "波斯尼亚和黑塞哥维那",
  "Belarus": "白俄罗斯",
  "Belize": "伯利兹",
  "Bermuda": "百慕大",
  "Bolivia": "玻利维亚",
  "Brazil": "巴西",
  "Barbados": "巴巴多斯",
  "Brunei": "文莱",
  "Bhutan": "不丹",
  "Botswana": "博茨瓦纳",
  "Central African Rep.": "中非",
  "Canada": "加拿大",
  "Switzerland": "瑞士",
  "Chile": "智利",
  "China": "中国",
  "Côte d'Ivoire": "科特迪瓦",
  "Cameroon": "喀麦隆",
  "Dem. Rep. Congo": "刚果民主共和国",
  "Congo": "刚果",
  "Colombia": "哥伦比亚",
  "Cape Verde": "佛得角",
  "Costa Rica": "哥斯达黎加",
  "Cuba": "古巴",
  "N. Cyprus": "北塞浦路斯",
  "Cyprus": "塞浦路斯",
  "Czech Rep.": "捷克",
  "Germany": "德国",
  "Djibouti": "吉布提",
  "Denmark": "丹麦",
  "Dominican Rep.": "多米尼加",
  "Algeria": "阿尔及利亚",
  "Ecuador": "厄瓜多尔",
  "Egypt": "埃及",
  "Eritrea": "厄立特里亚",
  "Spain": "西班牙",
  "Estonia": "爱沙尼亚",
  "Ethiopia": "埃塞俄比亚",
  "Finland": "芬兰",
  "Fiji": "斐济",
  "France": "法国",
  "Gabon": "加蓬",
  "United Kingdom": "英国",
  "Georgia": "格鲁吉亚",
  "Ghana": "加纳",
  "Guinea": "几内亚",
  "Gambia": "冈比亚",
  "Guinea-Bissau": "几内亚比绍",
  "Eq. Guinea": "赤道几内亚",
  "Greece": "希腊",
  "Grenada": "格林纳达",
  "Greenland": "格陵兰",
  "Guatemala": "危地马拉",
  "Guam": "关岛",
  "Guyana": "圭亚那",
  "Honduras": "洪都拉斯",
  "Croatia": "克罗地亚",
  "Haiti": "海地",
  "Hungary": "匈牙利",
  "Indonesia": "印度尼西亚",
  "India": "印度",
  "Br. Indian Ocean Ter.": "英属印度洋领土",
  "Ireland": "爱尔兰",
  "Iran": "伊朗",
  "Iraq": "伊拉克",
  "Iceland": "冰岛",
  "Israel": "以色列",
  "Italy": "意大利",
  "Jamaica": "牙买加",
  "Jordan": "约旦",
  "Japan": "日本",
  "Siachen Glacier": "锡亚琴冰川",
  "Kazakhstan": "哈萨克斯坦",
  "Kenya": "肯尼亚",
  "Kyrgyzstan": "吉尔吉斯坦",
  "Cambodia": "柬埔寨",
  "Korea": "韩国",
  "Kuwait": "科威特",
  "Lao PDR": "老挝",
  "Lebanon": "黎巴嫩",
  "Liberia": "利比里亚",
  "Libya": "利比亚",
  "Sri Lanka": "斯里兰卡",
  "Lesotho": "莱索托",
  "Lithuania": "立陶宛",
  "Luxembourg": "卢森堡",
  "Latvia": "拉脱维亚",
  "Moldova": "摩尔多瓦",
  "Madagascar": "马达加斯加",
  "Mexico": "墨西哥",
  "Macedonia": "马其顿",
  "Mali": "马里",
  "Malta": "马耳他",
  "Myanmar": "缅甸",
  "Montenegro": "黑山",
  "Mongolia": "蒙古",
  "Mozambique": "莫桑比克",
  "Mauritania": "毛里塔尼亚",
  "Mauritius": "毛里求斯",
  "Malawi": "马拉维",
  "Malaysia": "马来西亚",
  "Namibia": "纳米比亚",
  "New Caledonia": "新喀里多尼亚",
  "Niger": "尼日尔",
  "Nigeria": "尼日利亚",
  "Nicaragua": "尼加拉瓜",
  "Netherlands": "荷兰",
  "Norway": "挪威",
  "Nepal": "尼泊尔",
  "New Zealand": "新西兰",
  "Oman": "阿曼",
  "Pakistan": "巴基斯坦",
  "Panama": "巴拿马",
  "Peru": "秘鲁",
  "Philippines": "菲律宾",
  "Papua New Guinea": "巴布亚新几内亚",
  "Poland": "波兰",
  "Puerto Rico": "波多黎各",
  "Dem. Rep. Korea": "朝鲜",
  "Portugal": "葡萄牙",
  "Paraguay": "巴拉圭",
  "Palestine": "巴勒斯坦",
  "Qatar": "卡塔尔",
  "Romania": "罗马尼亚",
  "Russia": "俄罗斯",
  "Rwanda": "卢旺达",
  "Saudi Arabia": "沙特阿拉伯",
  "Sudan": "苏丹",
  "S. Sudan": "南苏丹",
  "Senegal": "塞内加尔",
  "Singapore": "新加坡",
  "Solomon Is.": "所罗门群岛",
  "Sierra Leone": "塞拉利昂",
  "El Salvador": "萨尔瓦多",
  "Suriname": "苏里南",
  "Slovakia": "斯洛伐克",
  "Slovenia": "斯洛文尼亚",
  "Sweden": "瑞典",
  "Swaziland": "斯威士兰",
  "Seychelles": "塞舌尔",
  "Syria": "叙利亚",
  "Chad": "乍得",
  "Togo": "多哥",
  "Thailand": "泰国",
  "Tajikistan": "塔吉克斯坦",
  "Turkmenistan": "土库曼斯坦",
  "Timor-Leste": "东帝汶",
  "Tonga": "汤加",
  "Trinidad and Tobago": "特立尼达和多巴哥",
  "Tunisia": "突尼斯",
  "Turkey": "土耳其",
  "Tanzania": "坦桑尼亚",
  "Uganda": "乌干达",
  "Ukraine": "乌克兰",
  "Uruguay": "乌拉圭",
  "United States": "美国",
  "Uzbekistan": "乌兹别克斯坦",
  "Venezuela": "委内瑞拉",
  "Vietnam": "越南",
  "Vanuatu": "瓦努阿图",
  "Yemen": "也门",
  "South Africa": "南非",
  "Zambia": "赞比亚",
  "Zimbabwe": "津巴布韦",
  "Aland": "奥兰群岛",
  "American Samoa": "美属萨摩亚",
  "Fr. S. Antarctic Lands": "南极洲",
  "Antigua and Barb.": "安提瓜和巴布达",
  "Comoros": "科摩罗",
  "Curaçao": "库拉索岛",
  "Cayman Is.": "开曼群岛",
  "Dominica": "多米尼加",
  "Falkland Is.": "马尔维纳斯群岛（福克兰）",
  "Faeroe Is.": "法罗群岛",
  "Micronesia": "密克罗尼西亚",
  "Heard I. and McDonald Is.": "赫德岛和麦克唐纳群岛",
  "Isle of Man": "曼岛",
  "Jersey": "泽西岛",
  "Kiribati": "基里巴斯",
  "Saint Lucia": "圣卢西亚",
  "N. Mariana Is.": "北马里亚纳群岛",
  "Montserrat": "蒙特塞拉特",
  "Niue": "纽埃",
  "Palau": "帕劳",
  "Fr. Polynesia": "法属波利尼西亚",
  "S. Geo. and S. Sandw. Is.": "南乔治亚岛和南桑威奇群岛",
  "Saint Helena": "圣赫勒拿",
  "St. Pierre and Miquelon": "圣皮埃尔和密克隆群岛",
  "São Tomé and Principe": "圣多美和普林西比",
  "Turks and Caicos Is.": "特克斯和凯科斯群岛",
  "St. Vin. and Gren.": "圣文森特和格林纳丁斯",
  "U.S. Virgin Is.": "美属维尔京群岛",
  "Samoa": "萨摩亚"
}


"""
map = Map().add(series_name="世界疫情分布",
                data_pair=data_list_all,
                maptype="world",
                name_map=nameMap,
                is_map_symbol_show=False
)

map.set_global_opts(title_opts=opts.TitleOpts(title="世界疫情（累计确诊）"),
                    visualmap_opts=opts.VisualMapOpts(max_=2900000,is_piecewise=True))
map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map.render('世界疫情（累计确诊）.html')


"""


map1 = Map().add(series_name="世界疫情分布",
                data_pair=data_list_new,
                maptype="world",
                name_map=nameMap,
                is_map_symbol_show=False
)

map1.set_global_opts(title_opts=opts.TitleOpts(title="世界疫情（新增确诊）"),
                    visualmap_opts=opts.VisualMapOpts(max_=58000,is_piecewise=True))
map1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map1.render('世界疫情（新增确诊）.html')


"""
map2 = Map().add(series_name="世界疫情分布",
                data_pair=data_list_dead,
                maptype="world",
                name_map=nameMap,
                is_map_symbol_show=False
)

map2.set_global_opts(title_opts=opts.TitleOpts(title="世界疫情（死亡）"),
                    visualmap_opts=opts.VisualMapOpts(max_=140000,is_piecewise=True))
map2.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map2.render('世界疫情（死亡）.html')




map3 = Map().add(series_name="世界疫情分布",
                data_pair= data_list_heal,
                maptype="world",
                name_map=nameMap,
                is_map_symbol_show=False
)

map3.set_global_opts(title_opts=opts.TitleOpts(title="世界疫情（治疗）"),
                    visualmap_opts=opts.VisualMapOpts(max_=1200000,is_piecewise=True))
map3.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map3.render('世界疫情（治疗）.html')
"""
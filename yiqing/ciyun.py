from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


song_url = "https://music.163.com/discover/toplist?id=3778678"
# comment_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_516997458?limit=20&offset=40"

driver_path = "chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
drive = webdriver.Chrome(driver_path, chrome_options=chrome_options)

headers = {
    "Host": "music.163.com",
    "Referer": "https://music.163.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


def getSoup(url):
    drive.get(url)
    iframe = drive.find_elements_by_id('g_iframe')[0]
    drive.switch_to.frame(iframe)
    return BeautifulSoup(drive.page_source, "lxml")


# 获取歌曲信息
def getAllSong():
    soup = getSoup(song_url)
    nodes = soup.select(".m-table-rank tbody tr")
    players = []
    for node in nodes:
        rank = node.select_one(".num").get_text()
        song_href = "https://music.163.com" + node.select("td")[1].select_one("a")["href"]
        song_name = node.select("td")[1].select_one("b")["title"]
        song_id = node.select_one(".ply")["data-res-id"]
        song_time = node.select("td")[2].select_one(".u-dur").get_text()
        song_player = node.select("td")[3].select_one("span")["title"]

        song_info = {
            "rank": rank,
            "song_href": song_href,
            "song_name": song_name,
            "song_id": song_id,
            "song_time": song_time,
            "song_player": song_player
        }
        players.append(song_info)
    return players


def getComments(song_href):
    soup = getSoup(song_href)
    time.sleep(0.1)
    comment_nodes = soup.select(".cmmts .itm")
    comments = []
    for node in comment_nodes:
        comment_user = node.select_one(".s-fc7").get_text()
        comment_content = node.select_one(".f-brk").get_text()
        comment_content_str = str(comment_content).split("：")[1]
        comment_time = node.select_one("div .time").get_text()
        comment_thumb_up = node.select_one("div .rp a").get_text()
        comment_thumb_up_str = str(comment_thumb_up).replace("(", "").replace(")", "").strip()

        if (comment_thumb_up_str.find("万") > 0 or (comment_thumb_up_str.strip() != '回复' and
                                                   comment_thumb_up_str.strip() != '' and int(
                    comment_thumb_up_str) > 1000)):
            comment = {"user": comment_user,
                       "content": comment_content_str,
                       "time": comment_time,
                       "thumb_up": comment_thumb_up_str}

            comments.append(comment)
        com = pd.DataFrame(comments)
    return com


if __name__ == '__main__':
    list_songs = getAllSong()
    for song in list_songs:
        try:
            name = 'comment/'+ song['song_name'] + '  ' +song['song_player'] + ".txt"
            f = open(name ,"ab+")
        except:
            name = 'comment/Love is Gone.txt'
            f = open(name,'ab+')
        print(song)
        comments = getComments(song["song_href"])
        print(comments['content'])
        print("-" * 50)
        f.close()
        time.sleep(0.1)
    drive.quit()

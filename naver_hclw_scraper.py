import time

import codecs
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from io import BytesIO
from PIL import Image


def get_chapters():
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome()
    i = 28
    arr_of_chapters = []
    while i>0:
        driver.get(
            'https://comic.naver.com/webtoon/list.nhn?titleId=670152&page=' + str(i))
        html = driver.page_source
        page_soup = BeautifulSoup(html, features='html.parser')
        chapter_list_container = page_soup.find("table", {'class': 'viewList'}).find("tbody").find_all("tr", {'class': ''})
        arr_of_chapters_flipped = []
        for chapter in chapter_list_container:
            url = chapter.find('a').attrs['href']
            name = chapter.find('td', {'class': 'title'}).text.strip()
            rating = chapter.find('div', {'class': 'rating_type'}).text.strip()[3:]
            chapter_info = {
                'url': 'https://comic.naver.com' + url,
                'name': name,
                'len': '',
                'rating': rating
            }
            # sends formatted information to function that will posts to database
            arr_of_chapters_flipped.insert(0, chapter_info)
        arr_of_chapters += arr_of_chapters_flipped
        i-=1
    driver.close()
    get_chapter_length(arr_of_chapters)
    

def get_chapter_length(arr_of_chapters):
    hclw_chapters_txt = open("naver_hclw_chapters.txt","w", encoding="utf-16")
    arr_of_chapters_without_link = []
    driver = webdriver.Chrome()
    arr_of_chapter_len = []
    for chapter in arr_of_chapters: 
        driver.get(chapter['url'])
        html = driver.page_source
        page_soup = BeautifulSoup(html, features='html.parser')
        chapter_img_list_container = page_soup.find("div", {'class': 'wt_viewer'})
        chapter_len = 0
        for img in chapter_img_list_container.find_all('img'):
            image_raw = get(img.get('src'), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'})
            image = Image.open(BytesIO(image_raw.content))
            width, height = image.size
            chapter_len += int(height)

        time.sleep(1)
        participation = driver.find_element_by_class_name('pointTotalPerson').text[4:-1]
        driver.switch_to.frame(driver.find_element_by_id("commentIframe"))
        comment_count = driver.find_element_by_class_name('u_cbox_count').text.replace(',','')
        obj = {
            "name": "" + chapter['name'] + "",
            "length": chapter_len,
            "rating": chapter['rating'],
            "participation": participation,
            "comments": int(comment_count)
        }
        print(obj)
        hclw_chapters_txt.write(repr(obj) + '\n')
    driver.close()



if __name__ == "__main__":
    get_chapters()

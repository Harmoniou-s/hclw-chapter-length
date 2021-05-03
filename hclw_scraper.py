import time

from bs4 import BeautifulSoup
from selenium import webdriver


def get_chapters():
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome()
    i = 28
    arr_of_chapters = []
    while i>0:
        driver.get(
            'https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221&page=' + str(i))
        html = driver.page_source
        page_soup = BeautifulSoup(html, features='html.parser')
        chapter_list_container = page_soup.find("ul", {'id': '_listUl'})
        arr_of_chapters_flipped = []
        for chapter in chapter_list_container.find_all('a'):
            
            url = chapter.attrs['href']
            name = chapter.find('span', {'class': 'subj'}).text.strip()
            
            chapter_info = {
                'url': url,
                'name': name,
                'len': ''
            }
            # sends formatted information to function that will posts to database
            arr_of_chapters_flipped.insert(0, chapter_info)
        arr_of_chapters += arr_of_chapters_flipped
        i-=1
    driver.close()
    get_chapter_length(arr_of_chapters)

def get_chapter_length(arr_of_chapters):
    hclw_chapters_txt = open("hclw_chapters.txt","w")
    arr_of_chapters_without_link = []
    driver = webdriver.Chrome()
    arr_of_chapter_len = []
    for chapter in arr_of_chapters: 
        driver.get(chapter['url'])
        html = driver.page_source
        page_soup = BeautifulSoup(html, features='html.parser')
        chapter_img_list_container = page_soup.find("div", {'id': '_imageList'})
        chapter_len = 0
        for img in chapter_img_list_container.select('img'):
            chapter_len += int(img.get('height')[:-2])
        obj = {
            "name": "" + chapter['name'] + "",
            "length": chapter_len
        }
        print(obj)
        hclw_chapters_txt.write(repr(obj) + '\n')
    driver.close()



if __name__ == "__main__":
    get_chapters()

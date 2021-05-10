import time

import json
from bs4 import BeautifulSoup
from selenium import webdriver


def get_chapters(start, end):
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome()
    i = start
    arr_of_chapters = []
    while i>end:
        driver.get(
            'https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221&page=' + str(i))
        html = driver.page_source
        page_soup = BeautifulSoup(html, features='html.parser')
        chapter_list_container = page_soup.find("ul", {'id': '_listUl'})
        arr_of_chapters_flipped = []
        for chapter in chapter_list_container.find_all('a'):
            
            url = chapter.attrs['href']
            name = chapter.find('span', {'class': 'subj'}).text.strip()
            likes = chapter.find('span', {'class': 'like_area'}).text.strip().replace('like', '').replace(',','')
            chapter_info = {
                'url': url,
                'name': name,
                'len': '',
                'likes': int(likes)
            }
            # sends formatted information to function that will posts to database
            arr_of_chapters_flipped.insert(0, chapter_info)
        arr_of_chapters += arr_of_chapters_flipped
        i-=1
    driver.close()
    return get_chapter_length(arr_of_chapters)

def scrape_latest():
    chapter_text = open("hclw_chapters.txt","a")
    readable_text = open("hclw_chapters.txt","r")
    latest_chapters_from_text = readable_text.readlines()[-15:]
    if latest_chapters_from_text[-1] != '\n':
        chapter_text.write("\n")
    latest_chapters_from_scrape = get_chapters(1, 0)
    for scrape_chapter in latest_chapters_from_scrape:
        #checks if chapter is in text file
        scrape_chapter = json.loads(scrape_chapter.replace("'", ''))
        add_chapter = True
        for chapter in latest_chapters_from_text:
            if chapter == '\n':
                continue
            chapter = json.loads(chapter.replace('\n', ''))
            if scrape_chapter.get('name') == chapter.get('name'):
                add_chapter = False
                break
            else:
                add_chapter = True
        if add_chapter:
            print("Adding Chapter " + json.dumps(scrape_chapter))
            chapter_text.write(json.dumps(scrape_chapter) + "\n")

def get_chapter_length(arr_of_chapters, write=False):
    hclw_chapters = []
    driver = webdriver.Chrome()
    for chapter in arr_of_chapters: 
        driver.get(chapter['url'])
        html = driver.page_source
        page_soup = BeautifulSoup(html, features='html.parser')
        chapter_img_list_container = page_soup.find("div", {'id': '_imageList'})
        chapter_len = 0
        for img in chapter_img_list_container.select('img'):
            chapter_len += int(img.get('height')[:-2])
        time.sleep(1)
        comment_count = driver.find_element_by_class_name('u_cbox_count').text.replace(',','')
        obj = {
            "name":  chapter['name'],
            "length": chapter_len,
            "likes": chapter['likes'],
            "comments": int(comment_count)
        }
        hclw_chapters.append(json.dumps(obj))
    if write:
        write_chapters(hclw_chapters)
    driver.close()
    return hclw_chapters

def write_chapters(chapter_arr):
    hclw_chapters_txt = open("hclw_chapters.txt","w")
    for chapter in chapter_arr:
        hclw_chapters_txt.write(repr(chapter).replace("'", '') + '\n')

if __name__ == "__main__":
    scrape_latest()

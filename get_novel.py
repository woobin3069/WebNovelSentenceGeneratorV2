from selenium import webdriver
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://novel.munpia.com/page/hd.novel/group/nv.pro/gpage/6")

novels=[]
novel_links=[]
novels = driver.find_elements_by_class_name("title")
for novel in novels:
    novel_links.append(novel.get_attribute("href"))
print("Successfully Get Links : ")

output = ''
print(novel_links)
f = open('output.txt', 'w', -1, 'utf-8')
print(len(novel_links))
for i in tqdm(range(0, len(novel_links))):
    if not novel_links[i]:
        break
    driver.get(novel_links[i])
    first_view = driver.find_element_by_class_name("first-view")
    first_view.click()

    novel_page = driver.find_element_by_class_name("tcontent")
    novel_text = novel_page.find_elements_by_tag_name("p")
    for text in novel_text:
        f.write(text.text + "\n")
        # output += (text.text + "\n")
        # print(output)
f.close()

# print("Done, output is")
# print(output)
# print("writing our file...")
#
#

print("Writing complete")
from time import sleep
from recipe_scraper import scrap_recipe

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


recipe_objects = scrap_recipe()#レシピの取得
chrome_path = '/Users/akaunntomei/Desktop/django_scraping/chromedriver'

#ブログの管理者ページへアクセス
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'http://127.0.0.1:8000/admin/'
driver.get(url)

sleep(3)

#管理者ページからログインする
user_name = 'tsubasa'
user_form = driver.find_element_by_name('username')
user_form.send_keys(user_name)
sleep(1)

password = 'user1234'
pass_form = driver.find_element_by_name('password')
pass_form.send_keys(password)
sleep(1)

rogin_btn = driver.find_element_by_xpath('//input[@type="submit"]')
rogin_btn.click()

sleep(3)

#追加ボタンを押す
add_link = driver.find_element_by_class_name('addlink')
add_link.click()
sleep(1)

#postを保存する（全てのレシピに対してループ）
for recipe in recipe_objects:
   
    #投稿内容を入力
    
    author = driver.find_element_by_id('id_author')
    author_select = Select(author)
    author_select.select_by_value('1')

    Title = driver.find_element_by_class_name('vTextField')
    Title.send_keys(recipe.title)
    sleep(1)

    Text = driver.find_element_by_class_name('vLargeTextField')
    Text.send_keys(recipe.text)
    sleep(1)
    
    #投稿日時を指定
    
    published_date = driver.find_element_by_class_name('field-published_date')

    published_day = published_date.find_element_by_link_text('今日')
    published_day.click()

    published_time = published_date.find_element_by_link_text('現在')
    published_time.click()

    save = driver.find_element_by_name('_addanother')
    save.click()




driver.quit()


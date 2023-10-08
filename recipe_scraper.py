import requests
from bs4 import BeautifulSoup



#スクレイピングのメソッドを作成
def scrap_recipe():
    
    url = 'https://www.orangepage.net/recipes/search/421?page={}'
    recipe_title_list = []
    recipe_text_list = []
    
    #1ページ目から3ページ目までをループ
    for page in range(1,4):

        target_url = url.format(page)
        res = requests.get(target_url)
        soup = BeautifulSoup(res.text,'lxml')

        recipe_list = soup.find('div',class_='recipesList recipesList--list active' )
        recipes = recipe_list.find_all('li')

        #全てのレシピに対してループ   
        for recipe in recipes:
            #スポンサーのレシピをスキップ
            if "sponsored" in recipe.get('class',[]):
                continue
            
            #レシピからタイトルを取り出す
            recipe_title = recipe.find('h2',class_='tit').text

            #レシピからレシピのテキストを取り出す：if文でテキストがない場合の対処をする
            recipe_text = recipe.find('p',class_='txt').text
            if recipe_text == '':
                recipe_text = 'テキストなし'
            else:
                recipe_text = recipe_text


            recipe_title_list.append(recipe_title)
            recipe_text_list.append(recipe_text)
            
    return recipe_title_list,recipe_text_list

scrap_recipe()
    

    


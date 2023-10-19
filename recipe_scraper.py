from recipe import Recipe, RecipeFactory, InputValueException
import requests

from bs4 import BeautifulSoup



#スクレイピングのメソッドを作成
def fetch_recipe():
    
    url = 'https://www.orangepage.net/recipes/search/421?page={}'
    recipe_objects = []
    
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
            scraped_recipe_title = recipe.find('h2',class_='tit').text

            #レシピからレシピのテキストを取り出す：if文でテキストがない場合の対処をする
            scraped_recipe_text = recipe.find('p',class_='txt').text
            
            try:
                recipe_object = RecipeFactory.create_recipe(scraped_recipe_title, scraped_recipe_text)
                recipe_objects.append(recipe_object)
            
            except InputValueException as e:
                # エラーが発生した場合はその内容を出力
                print(f"An error occurred: {e}")  # エラーが発生した場合はその内容を出力
            
        
            
    return recipe_objects


    



class Recipe:
    def __init__(self, title, text):
        self.title = title
        self.text = text

#title,textが無効な場合に発生
class InputValueException(Exception):
    pass


class RecipeFactory:
    @staticmethod
    def create_recipe(title: str, text: str):
        
        if not isinstance(title, str) or title == "":
            raise InputValueException("title should not be empty")
        
        if text == "":
            # titleが有効な場合のみ
            if title:  
                text = "テキストなし"
        
        return Recipe(title, text)
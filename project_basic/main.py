from fastapi import FastAPI,Body
from pydantic import BaseModel
from data import data_recipes
app = FastAPI()
import logging

recipes=data_recipes['recipes']

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api-recepies")
async def recipes_api():
    
    return recipes

@app.get("/app-recipes/{recipe_id}")
async def recipe_api_id(recipe_id:int):
    recipe=recipes[recipe_id-1]
    return {"Recepie": recipe}

# parameters
@app.get("/app-recipes_name/{recipe_name}")
async def recipe_api_name(recipe_name:str):
    for recipe in recipes:
        if recipe.get('name').casefold()==recipe_name.casefold():
            return {"Recepie": recipe}
        else:
            return { "Recipe":"Not Found"}
    
# query paramaters

@app.get("/app-recipe-qp/")
async def recipe_api_qp(ingredient:str):
    recipes_filters=[]
    for recipe in recipes:
            for ingredient_list_iten in recipe.get('ingredients'):
                if ingredient.casefold() in ingredient_list_iten.casefold():
                    logging.info(recipe.get('ingredients'))
                    recipes_filters.append(recipe)
    if len(recipes_filters)>0:
        return {"Recipes":recipes_filters}
    else:
        return { "Recipe":"No Recipe Found with "+ingredient}


class Recipe(BaseModel):
    id:int
    name:str
    ingredients:list
    instructions:list
    prepTimeMinutes: int
    cookTimeMinutes:int
    servings:int
    difficulty:str
    cuisine:str
    caloriesPerServing:int
    tags:list
    userId: int
    image:str
    rating:float
    reviewCount:int
    mealType:list
# request body/post request

@app.post("/create_recipe")
async def recipe_new(new_recipe: Recipe):
    logging.info(new_recipe)
    return new_recipe


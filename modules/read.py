import numpy as np
import pandas as pd
import pickle
import os
import streamlit as st

def read_book(book_selection):

   
    if book_selection in os.listdir("cocktail_books"):

        with open(file = f"cocktail_books/{book_selection}", mode = "rb") as file:
            book = pickle.load(file = file)

    else:
        raise Exception("No Book.")

    return book

def read_ingredients(cocktails):

    all_ingredients = list()

    for cocktail in cocktails:
        cocktail_ingredients = np.array(cocktail.get("ingredients"))[:, 1]
        cocktail_ingredients = [ingredient.lower() for ingredient in cocktail_ingredients]

        all_ingredients.extend(cocktail_ingredients)

    unique_ingredients = list(set(all_ingredients))

    unique_ingredients = pd.Series(unique_ingredients).sort_values()

    return unique_ingredients
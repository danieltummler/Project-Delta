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


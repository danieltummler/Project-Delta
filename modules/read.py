import numpy as np
import pandas as pd
import pickle
import os
import streamlit as st

def read_book():

    book_name = st.selectbox(label = "Book Name",
                             options = ["experimental_cocktail_club_book.pkl", "fenix_cocktail_bar_book.pkl"],
                             index = 1)

    # books = os.listdir()
  
    if book_name:

        with open(file = book_name, mode = "rb") as file:
            book = pickle.load(file = file)

    else:
        raise Exception("No Book.")

    return book


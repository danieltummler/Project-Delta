import numpy as np
import pandas as pd
import pickle
import os
import streamlit as st

def read_book(book_name = "experimental_cocktail_club_book.pkl"):

    # books = os.listdir()
  
    # if book_name in books:

    with open(file = book_name, mode = "rb") as file:
        book = pickle.load(file = file)

    # else:
    #     raise Exception("No Book.")

    return book


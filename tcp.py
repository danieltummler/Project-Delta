import streamlit as st
import numpy as np
import pandas as pd
from modules import read
from modules import write

def main():

    st.title("Project $\Delta$")

    book = read.read_book()

    # with st.sidebar:
    #     write.show_list_cocktails_from_book(book)

    cocktail_info = write.show_cocktail_matrix(book = book)

    write.show_cocktail(cocktail_info = cocktail_info)



if __name__ == "__main__":
    main()
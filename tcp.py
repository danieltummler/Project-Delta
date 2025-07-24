import streamlit as st
import numpy as np
import pandas as pd
from modules import read
from modules import write

def main():

    st.markdown("# $\\nabla$")

    book = read.read_book()

    # with st.sidebar:
    #     write.show_list_cocktails_from_book(book)

    cocktail_info = write.show_cocktail_matrix(book = book)

    write.show_cocktail(cocktail_info = cocktail_info)
    try:
        write.show_picture(cocktail_info = cocktail_info)
    except:
        st.write("No pictures.")



if __name__ == "__main__":
    main()

import streamlit as st
import numpy as np
import os
from modules import read
from modules import write

st.set_page_config(page_title = " ∇ The Cocktail Project", page_icon = "∇", layout = "wide")

def main():

    st.markdown(body = "# $\\nabla$")

    # Queda presentable, pero no hace referencia al archivo original
    # cocktail_books = [book.split("_", maxsplit = 1)[1].strip(".pkl").replace("_", " ").title() for book in os.listdir("cocktail_books")]

    cocktail_books = [book for book in os.listdir("cocktail_books")]
    book_selection = st.sidebar.selectbox(options = cocktail_books, label = "Cocktail Books")

    book = read.read_book(book_selection = book_selection)

    book_menu = st.segmented_control(label = "Menu", options = ["Cocktails", "Homemade Ingredients", "Charts"])

    if book_menu == "Cocktails":
        st.markdown(body = f"### {book_selection.split('_', maxsplit = 1)[1].strip('.pkl').replace('_', ' ').title()}")

        cocktails = book["cocktails"]

        ingredient_filter = st.selectbox(label = "Ingredient",
                                         options = read.read_ingredients(cocktails = cocktails),
                                         index = None,
                                         placeholder = "Select an ingredient")

        col1, col2, col3, col4 = st.columns([1 for x in range(4)])

        cocktails_filtered = [cocktail for cocktail in cocktails if ingredient_filter in [x.lower() for x in np.array(cocktail.get("ingredients"))[:, 1]]]

        if len(cocktails_filtered) == 0:

            for i in range(0, len(cocktails), 4):

                with col1.popover(f"{cocktails[i].get('name')}"):
                    write.ecc_popover_info(cocktails[i])
                try:
                    with col2.popover(f"{cocktails[i + 1].get('name')}"):
                        write.ecc_popover_info(cocktails[i + 1])
                except:
                    pass

                try:
                    with col3.popover(f"{cocktails[i + 2].get('name')}"):
                        write.ecc_popover_info(cocktails[i + 2])
                except:
                    pass

                try:
                    with col4.popover(f"{cocktails[i + 3].get('name')}"):
                        write.ecc_popover_info(cocktails[i + 3])
                except:
                    pass

        else:
            for i in range(0, len(cocktails_filtered), 4):

                with col1.popover(f"{cocktails_filtered[i].get('name')}"):
                    write.ecc_popover_info(cocktails_filtered[i])
                try:
                    with col2.popover(f"{cocktails_filtered[i + 1].get('name')}"):
                        write.ecc_popover_info(cocktails_filtered[i + 1])
                except:
                    pass

                try:
                    with col3.popover(f"{cocktails_filtered[i + 2].get('name')}"):
                        write.ecc_popover_info(cocktails_filtered[i + 2])
                except:
                    pass

                try:
                    with col4.popover(f"{cocktails_filtered[i + 3].get('name')}"):
                        write.ecc_popover_info(cocktails_filtered[i + 3])
                except:
                    pass


    elif book_menu == "Homemade Ingredients":
        st.markdown(body = "### Homemade Ingredients")

    else:
        pass


if __name__ == "__main__":
    main()
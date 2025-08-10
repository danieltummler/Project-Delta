import streamlit as st
import os

def show_list_cocktails_from_book(book):

    list_books = [cocktail["name"] for cocktail in book if "name" in cocktail]

    st.write(list_books)

def show_cocktail_matrix(book):

    list_books = [cocktail["name"] for cocktail in book if "name" in cocktail]
    # option_map = {num : cocktail_name for num, cocktail_name in enumerate(list_books)}

    selection = st.pills(label = "Cocktails",
                         options = list_books,
                         selection_mode = "single",
                         default = list_books[-1])
    
    cocktail_info = [cocktail for cocktail in book if cocktail["name"] == selection][0]


    return cocktail_info

def show_cocktail(cocktail_info):

    st.write(f"#### {cocktail_info['name']}")
    st.divider()

    col1, col2 = st.columns([1, 2])

    
    col1.write("Ingredients:")
    for measure, ingredient in cocktail_info["ingredients"]:
        col1.write(f"{measure if '(' not in measure else measure.split(' ')[0]} - {ingredient}")

    for key in ["glass", "garnish", "directions"]:
        col2.write(f"{key.title()}: {cocktail_info[key] if cocktail_info[key] != '' else 'N/A'}")

def show_picture(cocktail_info):

    base_name = cocktail_info["name"].replace(" ", "_").lower()

    pictures_list = [x for x in os.listdir("pictures") if x.startswith(base_name)]    

    # path = f"pictures/{base_name}_0.jpg"

    for num, picture_name in enumerate(pictures_list):

        path = f"pictures/{picture_name}"

        st.image(image = path, caption = f"{cocktail_info['name']} - {num}")

def ecc_popover_info(cocktail_info):

    st.write(f"### {cocktail_info.get('name')}")
    st.divider()

    col1, col2 = st.columns([1, 2])

    
    col1.write("Ingredients:")
    for measure, ingredient in cocktail_info.get("ingredients"):
        col1.write(f"{measure if '(' not in measure else measure.split(' ')[0]} - {ingredient}")

    for key in ["glass", "garnish", "directions", "introduction", "page", "observations"]:
        col2.write(f"{key.title()}: {cocktail_info.get(key) if cocktail_info.get(key) not in ('', None) else 'N/A'}")
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu



with st.sidebar:
    selected = option_menu (
        menu_title="Main Menu",
        options=["Home", "Resources", "Contact"],
        icons=["house","book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            
        }
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Resources":
    st.title(f"You have selected { selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

# st.set_page_config(page_title='Survey Result')
st.header('heyo welcome to placement buddies :) ')
st.button('Log In')
st.button('Sign In')
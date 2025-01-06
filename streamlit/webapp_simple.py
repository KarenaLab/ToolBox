# Libraries
import numpy as np
import pandas as pd

import streamlit as st


# functions
def main_page():
    # Initial config
    st.set_page_config(page_title="Learning Streamlit",
                       initial_sidebar_state="collapsed")

    # Sidebar menu
    activity = ["intro", "option 1", "option 2", "option 3", "config"]
    choice = st.sidebar.selectbox("Menu", activity)

    # Pages
    if(choice == "intro"):
        page_intro()

    elif(choice == "option 1"):
        page_option1()

    elif(choice == "option 2"):
        page_option2()

    elif(choice == "option 3"):
        page_option3()

    elif(choice == "config"):
        page_config()
        

    return None


def page_intro():
    st.title("Learning Streamlit | Introduction")

    return None


def page_option1():
    st.title("Learning Streamlit | option 1")

    return None


def page_option2():
    st.title("Learning Streamlit | option 2")

    return None


def page_option3():
    st.title("Learning Streamlit | option 3")

    return None


def page_config():
    st.title("Learning Streamlit | Config")

    return None


# Program --------------------------------------------------------------
main_page()


# Instructions:
# To run this application: python -m streamlit run webapp_simple.py



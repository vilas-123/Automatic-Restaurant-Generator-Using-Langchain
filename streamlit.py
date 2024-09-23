import streamlit as st
from langchain_helper import generate

cuisine=st.sidebar.selectbox('pick a cuise ',('indian','russain','indonesia'))


if cuisine:
    response=generate(cuisine)
    st.title('Welcome you to ' + response['cuisine'])
    st.header(response['restaurant_name'])
    menu_items=response['menu_items'].split(',')
    st.write('menu ')
    for items in menu_items:
        st.write(items)    
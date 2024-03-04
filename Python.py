import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('all_data.csv')


st.title('E-commerce Public Data Analysis Dashboard')


st.sidebar.title('Options')
selected_option = st.sidebar.selectbox('Select an option', ['Product Sales', 'Customer Satisfaction'])


if selected_option == 'Product Sales':
    st.subheader('Product Sales Analysis')
    product_sales = data.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(product_sales)
    
elif selected_option == 'Customer Satisfaction':
    st.subheader('Customer Satisfaction Analysis')
    review_scores = data['review_score'].value_counts().sort_index()
    st.bar_chart(review_scores)
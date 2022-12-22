import pandas as pd
import numpy as np
import plotly.express as px
import warnings 
import streamlit as st
import plotly.figure_factory as ff
warnings.filterwarnings("ignore") 

st.title('Environmental Impact of Food')
st.header('Dataset')
st.write('Explanation of the entire dataset followed by Columns description.' )
# Data Exploration

my_dataset = pd.read_csv("./Cleaned_Food_Production-1.csv")
st.write(my_dataset.head(10))

livestock = ["Beef (beef herd)", "Beef (dairy herd)", "Lamb & Mutton", "Pig Meat", "Poultry Meat", "Fish (farmed)", "Shrimps (farmed)"]
grains = ["Wheat & Rye (Bread)", "Maize (Meal)", "Oatmeal", "Rice"]
fruitOrVeg = ["Potatoes", "Cassava", "Peas", "Tomatoes", "Onions & Leeks", "Root Vegetables", "Brassicas", "Citrus Fruit", "Other Vegetables", "Bananas", "Apples", "Berries & Grapes", "Other Fruit"]
oils = ["Soybean Oil", "Palm Oil", "Sunflower Oil", "Rapeseed Oil", "Olive Oil"]
dairy = ["Milk", "Cheese", "Eggs"]
other = ["Barley (Beer)", "Cane Sugar", "Beet Sugar", "Other Pulses", "Nuts", "Groundnuts", "Soymilk", "Tofu", "Wine", "Coffee", "Dark Chocolate"]


my_dataset["food_category"] = "category"

for i, row in my_dataset.iterrows():
    if row["Food product"] in livestock:
        my_dataset.loc[i,"food_category"] = "livestock"
    if row["Food product"] in grains:
        my_dataset.loc[i,"food_category"] = "grains"
    if row["Food product"] in fruitOrVeg:
        my_dataset.loc[i,"food_category"] = "fruitOrVeg"
    if row["Food product"] in oils:
        my_dataset.loc[i,"food_category"] = "oils"
    if row["Food product"] in dairy:
        my_dataset.loc[i,"food_category"] = "dairy"
    if row["Food product"] in other:
        my_dataset.loc[i,"food_category"] = "other"

st.header('Category of Food')
st.write('Explanation of how we categorized.' )
st.write(my_dataset.head(10))


# st.header('Value Counts For Each Feature')
# st.write(df['work_year'].value_counts())

category = my_dataset.groupby('food_category')
category_dataset = category.sum()

st.plotly_chart(px.imshow(category_dataset))
##### edited here


st.header('Drawing Conclusions')
st.write('Based on the exploration performed, we can conclude a few things. We can conclude that the salaries for Data Science and Data Analysis positions have a truly broad range, from $40k all the way to $600k with the majority hovering around $100k. We can conclude that fully remote positions generally earn more and are more popular within the industry, nearly twice as popular as both in-office and hybrid positions. An addition thing worth noting is that the majority of instances in this dataset are from the US, and the minority being from nearly every other continent.')
st.write('')

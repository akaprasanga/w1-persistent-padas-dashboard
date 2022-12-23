import pandas as pd
import numpy as np
import plotly.express as px
import warnings
import streamlit as st
import plotly.figure_factory as ff
warnings.filterwarnings("ignore")

st.title('Environmental Impact of Food')
st.header('Cool Team Behind This Project')

####### Team Description


st.write("Fiona Law:: Hi, I'm Fiona and I'm a sophomore at Woodbridge High School in California.")
st.write("Michael Jiang:: Hi, I'm Michael and I'm a freshman at the Gilman School in Baltimore, Maryland.")
st.write("Nikol Miasik:: Hi, my name is Nikol and I'm a senior at Stelly's Secondary School in BC, Canada.")
st.write("Edward Tang:: Hello, I am Edward and I am a freshman at Camas high school, Washington")
st.write("Prasanga Neupane:: Hi I am Prasanga and I am instructor of this group.")


#######


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
cols_to_move = ['Food product', 'food_category']
df = my_dataset[ cols_to_move + [ col for col in my_dataset.columns if col not in cols_to_move ] ]
st.write(df.head(100))


# st.header('Value Counts For Each Feature')
# st.write(df['work_year'].value_counts())

category = my_dataset.groupby('food_category')
category_dataset = category.sum()
st.write(category_dataset)
##### edited here
# fiona
st.header("Correlation Plot Between Food Categories and Columns")
st.write('In the correlation graph, it can be seen that most CO2 is emitted in the category of livestock. This includes beef herding, dairy herding, etc. In contrast, the fruit or veggie category and grains category yielded the smallest number of CO2 emissions. The dairy and oils category had the second fewest number of CO2 emissions and the "other" category was the category which had the second most CO2 emissions. Additionally, it is notable that the farm column released the most emissions when being compared to other columns.')
st.plotly_chart(px.imshow(category_dataset))

st.header("Histogram Chart of Land Use Changes")
fig1 = px.histogram(my_dataset, x="Land use change")
#fig1.show()
st.plotly_chart(fig1)

st.header("Histogram Chart of Total Emissions")
fig2 = px.histogram(my_dataset, x="Total_emissions")
#fig2.show()
st.plotly_chart(fig2)

st.write("While there isn't a distinct relationship between the total emissions of food production and land use changes, it can still be seen in the two histograms that when the land use changes were around 0 (meaning that human activities don't really effect the land), that was also when the total emissions are the least.")

##############fiona End line

######################Edward start here

st.header('Food Product and Processing')
st.write('The relationship between food product and processing')

fig = px.bar(my_dataset, x='Food product', y='Processing')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
#fig.show()
st.plotly_chart(fig)

st.header('Food Product and Transportation')
st.write('The relationship between food product and the transportation cost.')
fig = px.bar(my_dataset, x='Food product', y='Transport')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
#fig.show()
st.plotly_chart(fig)

#######################Edwards ending line


######################Michael start here
st.header('Livestock vs. Animal Feed')

fig = px.bar(my_dataset, x = 'Food product', y = 'Animal Feed')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)
st.write('Based on the bar graph, milk requires the least amount of animal feed in order to be produced. From the bar graph, we see that the proteins and other products such as cheese, milk, and eggs from farm animals requires a lot of animal feed to be produced')

st.header('The effect of food processing on carbon emissions')
st.plotly_chart(px.scatter(my_dataset, x = "Total_emissions", y = "Food product"))
st.write('Based on the scatter plot, food products that require more processing emit more carbon into the atmosphere. This can be due to the stages of processing that occur before each product is sold.')


#######################Michael ending line

######################Nikol start here
st.header('The Correlation Between Land Use Change and Total CO2 Emissions')
st.write('The first pie graph represents the total CO2 emissions of each food category. According to the pie graph above, we can see that livestock accounts for the highest amount of total CO2 emissions, with over 50%. This means that they use the highest amount of most of the category of emissions. Comparing the graph to the original data, it can be seen that the category with more farming is typically what has the highest total emissions output.')
st.plotly_chart(px.pie(my_dataset, values='Total_emissions', names='food_category'))

st.write('The pie graph shown below represents the land use change for each food category. Similarly to the total CO2 emissions graph, here you can see that livestock has a significantly higher amount of land use change, with just over 41%. The order of highest to lowest land use change is the exact same as the order of highest to lowest CO2 emissions, showing a clear correlation between the two.')
st.plotly_chart(px.pie(my_dataset, values='Land use change', names='food_category'))

st.header('Drawing Conclusions')
st.write('With the data and visualization we can conclude that livestock has the highest overall impact on CO2 emissions.')
st.write('')

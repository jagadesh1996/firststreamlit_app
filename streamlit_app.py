import streamlit

streamlit.title('Hotel HAJ')

streamlit.header('Breakfast Menu🥣')
streamlit.text('🥗 IDLY, POORI, DOSA, VADA, PONGAL')
streamlit.text('🍞 Boiled EGG, TEA, COFFEE, BISCUITS...')
streamlit.text('🐔 Biryani, Wings, 555....')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
